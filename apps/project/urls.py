from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required 

from .views import NewProjectFormView, DashboardView, ProjectDetailsView 


urlpatterns = patterns('',
        url(r'^new/$', login_required(NewProjectFormView.as_view()), name='project_new'),
        url(r'^dashboard/$', login_required(DashboardView.as_view()), name='project_dashboard'),
        url(r'^details/(\d+)/$', login_required(ProjectDetailsView.as_view()), name='poject_details'),
)
