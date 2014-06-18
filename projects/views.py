from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from .forms import NewProjectForm
from .models import NewProject

def new(request):
    if request.method == "GET":
        return render_to_response(
            'projects/new.html',
            { 'form' : NewProjectForm },
            context_instance=RequestContext(request)
        )
    elif request.method == "POST":
        form = NewProjectForm(request.POST, request.FILES)
        if not form.is_valid():
            return render_to_response(
                'projects/new.html',
                { 'form' : NewProjectForm },
                context_instance=RequestContext(request)
            )
        else:
            temp = NewProject(
                    name = form.cleaned_data["name"],
                    description = form.cleaned_data["description"],
                    upload_file = request.FILES['upload_file'],
                    ftp_file = form.cleaned_data["ftp_file"],
                    tissue = form.cleaned_data["tissue"],
                    disease = form.cleaned_data["disease"],
                    )
            temp.save()
            return HttpResponseRedirect(reverse('projects.views.dashboard'))
        

def dashboard(request):
    projects = NewProject.objects.all()
    return render(request,
                 'projects/dashboard.html',
                 { 'projects' : projects }, )

"""
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext


def new(request):
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = NewProject(docfile = request.FILES['docfile'])
            newdoc.save()
            #return HttpResponseRedirect(reverse(projects.views.new))
            return render('home.html')
    else:
        form = NewProjectForm()

    projects = NewProject.objects.all()

    return render_to_response(
        'projects/new.html',
        { 'projects' : projects, 'form' : form },
        context_instance = RequestContext(request)
    )


def new(request):
    if request.method == 'POST':
        return render(request,
                'projects/new.html',
                { 'form' : NewProjectForm })
    elif request.method == 'GET':
        return render(request,
                'projects/new.html',
                { 'form' : NewProjectForm })

"""
"""
def new(request):
    # Handle file upload
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            NewProject.objects.create(
                name = form.cleaned_data["name"],
                description = form.cleaned_data["description"],
                upload_file = request.FILES['upload_file'],
                ftp_file = form.cleaned_data["ftp_file"],
                tissue = form.cleaned_data["tissue"],
                disease = form.cleaned_data["disease"],
            )
            return HttpResponseRedirect(reverse('projects.views.dashboard'))
        else:
            form = NewProjectForm() 

    else:
        form = NewProjectForm() # A empty, unbound form

    return render_to_response(
        'projects/new.html',
        { 'form' : NewProjectForm },
        context_instance=RequestContext(request)
    )

"""
