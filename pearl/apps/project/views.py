import json

from django.core.urlresolvers import reverse 
from django.shortcuts import HttpResponseRedirect, render, HttpResponse
from django.views.generic.base import View 

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


def api(request, item, query):
    response_data = {}
    response_data['item'] = item
    response_data['query'] = query
    databases = {'tissues': MeshTissues, 'diseases': MeshDiseases}
    results = databases[item].objects.filter(descriptornamestring__icontains=query)[:10]
    data = [result.descriptornamestring for result in results]
    return HttpResponse(json.dumps(data),
                        content_type="application/json")
    
    
