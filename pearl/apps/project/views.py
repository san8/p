import json
from os.path import join

from .forms import NewProjectForm, StartProcessingForm
from .models import MeshDiseases, MeshTissues, NewProject, STATUS_CODES

from apps.accounts.models import Customer, Discount
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import HttpResponse, redirect
from django.views.generic import ListView
from django.views.generic.edit import FormView
from pearl.settings.base import NEW_PROJECT_URL


class NewProjectFormView(FormView):
    """
    Form to create a new project.
    """
    template_name = 'project/new.html'
    form_class = NewProjectForm
    success_url = '/project/dashboard'

    def form_valid(self, form):
        instance = form.save(commit=False)
        user = self.request.user
        instance.customer_id = user.id
        file_type = form.cleaned_data['file_type']
        if deduct_balance(user.id, file_type):
            instance.save()
            project_started(user.username, form.cleaned_data['name'])
            return super(NewProjectFormView, self).form_valid(form)
        else:
            return redirect("/account/insufficient-balance/")

    def get_context_data(self, **kwargs):
        context = super(NewProjectFormView, self).get_context_data(**kwargs)
        user_id = self.request.user.id
        balance = Customer.objects.get(user_id=user_id).balance

        if balance < settings.VCF_COST:
            message = ("You don't have enough balance to start a project."
                       " For more, contact info@leucinerichbio.com")
        elif settings.VCF_COST < balance < settings.FASTQ_COST:
            message = ("You don't have enough balance to start FASTQ project."
                       " For more, contact info@leucinerichbio.com")
        if 'message' in locals():
            context['message'] = message

        return context


def deduct_balance(user_id, file_type):
    """
    Deduct amount for a project.
    """
    if file_type == 'fastq':
        project_cost = settings.FASTQ_COST
        try:
            discount = Discount.objects.get(user=user_id).fastq
        except:
            discount = 0
    else:
        project_cost = settings.VCF_COST
        try:
            discount = Discount.objects.get(user=user_id).vcf
        except:
            discount = 0

    effective_cost = project_cost - discount
    balance = Customer.objects.get(user_id=user_id).balance

    if balance > effective_cost:
        Customer.objects.filter(user_id=user_id).update(
            balance=balance-effective_cost)
        return True
    return False


def project_started(user_name, project_name):
    """
    Send mail once a project is started.
    """
    message = """
    User name: {0}
    Project Number: {1}
    """.format(user_name, project_name)

    send_mail('New project started.', message,
              'noreply@leucinerichbio.com',
              ['admin@leucinerichbio.com', ])


class DashboardView(ListView):
    model = NewProject
    template_name = 'project/dashboard.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return NewProject.objects.filter(customer=self.request.user.id)\
                                 .order_by('-updated_at')

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        customer = Customer.objects.get(user_id=self.request.user.id)
        context['user_timezone'] = customer.timezone
        context['status_codes'] = STATUS_CODES
        return context


class QcReportView(FormView):
    """
    Show QC report to the user.
    Get conformation from user to start processing.
    """
    template_name = 'project/qc_report.html'
    form_class = StartProcessingForm
    success_url = '/project/dashboard'

    def get_context_data(self,  **kwargs):
        context = super(QcReportView, self).get_context_data(**kwargs)
        customer_id = self.request.user.id
        project_id = self.args[0]
        project = NewProject.objects.filter(customer_id=customer_id).get(
            id=project_id)
        context['project'] = project
        context['file_count'] = range(1, project.total_fastq_files+1)
        if project.status >= 2:
            from .tasks import fastq_qc_plus
            context['qc_data'] = (fastq_qc_plus(project_id))
            vcf = 'ctog' + str(project_id).zfill(6) + '.vcf'
            context['vcf_link'] = join(NEW_PROJECT_URL, str(project_id), vcf)
            csv = 'ctog' + str(project_id).zfill(6) + '_report' + '.csv'
            context['csv_link'] = join(NEW_PROJECT_URL, str(project_id), csv)

        return context

    def form_valid(self, form):
        form.save(commit=False)
        project_id = self.args[0]
        project = NewProject.objects.get(pk=project_id)
        project.start_processing = form.cleaned_data['start_processing']
        project.status = (-2, 3)[project.start_processing]
        project.save()
        return super(QcReportView, self).form_valid(form)


def api(request, item, query):
    response_data = {}
    response_data['item'] = item
    response_data['query'] = query
    databases = {'tissues': MeshTissues, 'diseases': MeshDiseases}
    results = databases[item].objects.filter(
        descriptornamestring__icontains=query)[:10]
    data = [result.descriptornamestring for result in results]
    return HttpResponse(json.dumps(data),
                        content_type="application/json")
