import json

from django.core.urlresolvers import reverse 
from django.shortcuts import HttpResponseRedirect, render, HttpResponse
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import FormView
from django.views.generic import ListView

from apps.accounts.models import Customer

from .models import NewProject, MeshTissues, MeshDiseases
from .models import STATUS_OPTIONS 
from .forms import NewProjectForm, StartProcessingForm


class NewProjectFormView(FormView):
    """
    Form to create a new project.
    """
    template_name = 'project/new.html'
    success_url = '/project/dashboard'
    form_class = NewProjectForm

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
        return NewProject.objects.filter(customer=self.request.user.id)
        
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        customer = Customer.objects.get(user_id=self.request.user.id)
        context['user_timezone'] = customer.timezone
        context['status_options'] = STATUS_OPTIONS
        return context
     

class QcReportView(View):
    """
    Show QC report to the user.
    Get conformation from user to start processing.
    """

    form_class = StartProcessingForm
    
    def get(self, request, project_id):
        form = StartProcessingForm()
        customer_id = request.user.id 
        project = NewProject.objects.filter(customer_id=customer_id).get(id=project_id)
        browser_stats = [['Chrome', 52.9], ['Firefox', 27.7], ['Opera', 1.6],
                         ['Internet Explorer', 12.6], ['Safari', 4]]

        return render(request, 'project/qc_report.html',
                      {'project': project, 'form': form, 'browser_stats': browser_stats},)

    def post(self, request, project_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            project = NewProject.objects.get(pk=project_id)
            project.start_processing = form.cleaned_data['start_processing']
            if project.start_processing:
                project.status = 3
            else:
                project.status = -2
            project.save() 
            return HttpResponseRedirect(reverse('project:project_dashboard'))
        return render(request, 'project/qc_report.html',)

        
def api(request, item, query):
    response_data = {}
    response_data['item'] = item
    response_data['query'] = query
    databases = {'tissues': MeshTissues, 'diseases': MeshDiseases}
    results = databases[item].objects.filter(descriptornamestring__icontains=query)[:10]
    data = [result.descriptornamestring for result in results]
    return HttpResponse(json.dumps(data),
                        content_type="application/json")
    
        
