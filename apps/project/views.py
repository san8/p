from django.core.urlresolvers import reverse 
from django.shortcuts import HttpResponseRedirect, render 
from django.views.generic.base import View 

from apps.accounts.models import Customer 
from .models import NewProject 
from .models import STATUS_OPTIONS 
from .models import DO_PROCESSING 
from .forms import NewProjectForm, StartProcessingForm 

from pearl.settings.base import REPORT_DIR 


class NewProjectFormView(View):
    form_class = NewProjectForm

    def get(self, request):
        form = NewProjectForm()
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

        
"""
class QcReportView(View):
    form = StartProcessingForm
    def get(self, request, project_id):
        form = StartProcessingForm() 
        customer_id = request.user.id 
        project = NewProject.objects.get(pk=project_id, customer_id=customer_id)
        links = project.qc_report_links()
        return render(request, 'project/qc_report.html', 
                {'project': project, 'links': links, 'form': form,
                    'REPORT_DIR': REPORT_DIR,},)

    def post(self, request, project_id):
        form = self.form(request.POST)
        project = NewProject.objects.get(pk=project_id)
        links = project.qc_report_links()
        if form.is_valid():
            project.start_processing = form.cleaned_data['start_processing']
            project.status = DO_PROCESSING 
            project.save() 
            return HttpResponseRedirect(reverse('project:project_dashboard'))
        return render(request, 'project/qc_report.html',
                {'project_id': project_id, 'links': links, 'form': form,})



class QcDetailsView(View):
    def get(self):
    #def get(self, project_id, report_dir):
        pass 


def json_data(request):
    data = []
    field = request.GET.get('field', '')
    query = request.GET.get('query', '')
    for q in DATA[field]:
        if query.lower() in q.lower():
            data.append(q)
    return HttpResponse(json.dumps(data), content_type="application/json")


class DashboardView(View):
    def get(self, request):
        projects = NewProject.objects.all()


def new(request):
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            newproject = NewProject(
                customer = request.user.id, 
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                #upload_file = request.FILES['upload_file'],
                #FTP_file = form.cleaned_data['FTP_file'],
                #tissues = form.cleaned_data['tissues'],
                #disease = form.cleaned_data['disease'],
            )
            newproject.save()
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = NewProjectForm()

    return render_to_response(
        'project/new.html',
        {'form': form},
        context_instance = RequestContext(request)
    )


class DashboardView2(ListView):
    model = NewProject 
"""

''' 
class ProjectDetailsView(View):
    def get(self, request, project_id):
        project_details = NewProject.objects.get(pk=project_id)
        if project_details.customer_id == request.user.id:
            return render(request, 'project/details.html', {'project_details': project_details,},)
        else:
            return HttpResponseNotFound('<h1>Page not found.</h1>')
''' 
