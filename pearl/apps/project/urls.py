from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = patterns(
    '',

    url(r'^new/$', login_required(views.NewProjectFormView.as_view()),
        name='project_new'),
    url(r'^dashboard/$', login_required(views.DashboardView.as_view()),
        name='project_dashboard'),
    url(r'^qcreport/(\d+)/$', login_required(views.QcReportView.as_view()),
        name='project_qcreport'),
    url(r'^api/(?P<item>\w+)/(?P<query>\w+)', views.api, name="data_api"),
)
