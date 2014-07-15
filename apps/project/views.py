from django.core.urlresolvers import reverse 
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect 
from django.views.generic.base import View 

from guardian.decorators import permission_required

from .models import NewProject 
from .forms import NewProjectForm 


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
        cust_id = request.session['_auth_user_id']
        myProjects = NewProject.objects.filter(customer=cust_id).order_by('updated_at')
        return render(request, 'project/dashboard.html', {'projects': myProjects},)


class ProjectDetailsView(View):
    def get(self, request, project_id):
        project_details = NewProject.objects.get(pk=project_id)
        return render(request, 'project/details.html', {'project_details': project_details,},)

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
