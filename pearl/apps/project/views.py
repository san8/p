from os.path import join
import json

from django.shortcuts import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic import ListView
from pearl.settings.base import NEW_PROJECT_URL

from apps.accounts.models import Customer

from .models import NewProject, MeshTissues, MeshDiseases
from .models import STATUS_OPTIONS
from .forms import NewProjectForm, StartProcessingForm


class NewProjectFormView(FormView):
    """
    Form to create a new project.
    """
    template_name = 'project/new.html'
    form_class = NewProjectForm
    success_url = '/project/dashboard'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.customer_id = self.request.user.id
        instance.save()
        return super(NewProjectFormView, self).form_valid(form)


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
        context['status_options'] = STATUS_OPTIONS
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
        project = NewProject.objects.get(id=project_id)
        context['project'] = project
        context['file_count'] = range(1, project.total_fastq_files+1)
        if project.status >= 2:
            from .tasks import fastq_qc_plus
            context['qc_data'] = (fastq_qc_plus(project_id))
            vcf = 'project' + str(project_id) + '.vcf'
            context['vcf_link'] = join(NEW_PROJECT_URL, str(project_id), vcf)
            csv = 'project' + str(project_id) + '_report' + '.csv'
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
    results = databases[item].objects.filter(descriptornamestring__icontains=query)[:10]
    data = [result.descriptornamestring for result in results]
    return HttpResponse(json.dumps(data),
                        content_type="application/json")
