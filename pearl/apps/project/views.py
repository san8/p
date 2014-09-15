import json

from django.core.urlresolvers import reverse 
from django.shortcuts import HttpResponseRedirect, render, HttpResponse
from django.views.generic.base import View
from django.views.generic.edit import FormView

#from pearl.settings.base import REPORT_DIR 
from apps.accounts.models import Customer 

from .models import NewProject, MeshTissues, MeshDiseases
from .models import STATUS_OPTIONS 
from .forms import NewProjectForm, StartProcessingForm


class NewProjectFormView(View):
    
    form_class = NewProjectForm

    def get(self, request):
        form = NewProjectForm(initial={'total_fastq_files': '1'})
        return render(request, 'project/new.html', {'form': form},)
   
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer_id = request.user.id 
            instance.save()
            return HttpResponseRedirect(reverse('project:project_dashboard'))
        return render(request, 'project/new.html', {'form': form},)


class DashboardView(View):
    
    def get(self, request):
        customer_id = request.user.id 
        customer = Customer.objects.get(user_id=customer_id)
        myProjects = NewProject.objects.filter(customer=customer_id)
        return render(request, 'project/dashboard.html', 
                {'projects': myProjects,
                 'status_options': STATUS_OPTIONS,
                 'user_timezone': customer.timezone,},)

    
class QcReportView(FormView):
    """
    Show QC report to the user.
    Get conformation from user to start processing.
    """
    
    def get(self, request, project_id):
        form = StartProcessingForm()
        customer_id = request.user.id 
        project = NewProject.objects.filter(customer_id=customer_id).get(id=project_id)
        return render(request, 'project/qc_report.html',
                      {'project': project, 'form': form,},)

    def post(self, request, project_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('project:project_dashboard'))
        return render(request, 'project/qc_report.html')

        
def api(request, item, query):
    response_data = {}
    response_data['item'] = item
    response_data['query'] = query
    databases = {'tissues': MeshTissues, 'diseases': MeshDiseases}
    results = databases[item].objects.filter(descriptornamestring__icontains=query)[:10]
    data = [result.descriptornamestring for result in results]
    return HttpResponse(json.dumps(data),
                        content_type="application/json")
    
        
    '''
    template_name ='project/qc_report.html'
    from_class = StartProcessingForm
    success_url = 'project/dashborad/'
    
    def form_valid(self, form):
        form.save()
        return super(QcReportView, self).form_valid(form)

        
    '''
 
