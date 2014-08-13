from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required 

from .views import NewProjectFormView, DashboardView


urlpatterns = patterns('',
        url(r'^new/$', login_required(NewProjectFormView.as_view()), name='project_new'),
        url(r'^dashboard/$', login_required(DashboardView.as_view()), name='project_dashboard'),
#        url(r'^qcreport/(\d+)/$', login_required(QcReportView.as_view()), name='project_qcreport'),
#        url(r'^qcdetails/(\d+)/(?P<dir_name>.+)/$', login_required(ProjectDetailsView.as_view()), name='project_qcdetails'),
#        url(r'^data/json/', json_data, name="json_data"),
)
