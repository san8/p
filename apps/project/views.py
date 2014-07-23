from django.core.urlresolvers import reverse 
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect 
from django.views.generic.base import View 
from django.http import HttpResponseNotFound 

from .models import NewProject 
from .models import STATUS_OPTIONS 
from .forms import NewProjectForm, StartProcessingForm 


class NewProjectFormView(View):
    form_class = NewProjectForm

    def get(self, request):
        form = NewProjectForm()
        return render(request, 'project/new.html', {'form': form},)
   
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer_id = request.session['_auth_user_id']
            if instance.total_fastq_files == '':
                instance.total_fastq_files = 0
            #instance.vcf_file = request.FILES['vcf_file']
            instance.save()
            return HttpResponseRedirect(reverse('project:project_dashboard'))
        return render(request, 'project/new.html', {'form': form},)


class DashboardView(View):
    def get(self, request):
        #cust_id = request.session['_auth_user_id']
        cust_id = request.user.id 
        myProjects = NewProject.objects.filter(customer=cust_id)
        return render(request, 'project/dashboard.html', 
                {'projects': myProjects,
                 'status_options': STATUS_OPTIONS},)

class ProjectDetailsView(View):
    def get(self, request, project_id):
        project_details = NewProject.objects.get(pk=project_id)
        if project_details.customer_id == request.user.id:
            return render(request, 'project/details.html', {'project_details': project_details,},)
        else:
            return HttpResponseNotFound('<h1>Page not found.</h1>')


class QcReportView(View):
    form = StartProcessingForm
    def get(self, request, project_id):
        form = StartProcessingForm() 
        project = NewProject.objects.get(pk=project_id)
        links = project.qc_report_links()
        if project.customer_id == request.user.id:
            return render(request, 'project/qc_report.html', 
                    {'project_id': project_id, 'links': links, 'form': form,},)
        else:
            return HttpResponseNotFound('<h1>Page Not Found.</h1>')

    def post(self, request, project_id):
        form = self.form(request.POST)
        project = NewProject.objects.get(pk=project_id)
        links = project.qc_report_links()
        if form.is_valid():
            project.start_pocessing = form.cleaned_data['start_pocessing']
            project.save() 
            return HttpResponseRedirect(reverse('project:project_dashboard'))
        return render(request, 'project/qc_report.html',
                {'project_id': project_id, 'links': links, 'form': form,})


class QcDetailsView(View):
    def get(self):
    #def get(self, project_id, report_dir):
        pass 


"""
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
