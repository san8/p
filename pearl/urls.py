from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.home.views import HomeView 


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', HomeView.as_view()),
    url(r'^home/', include('apps.home.urls', namespace='home')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^accounts/', include('allauth.urls', namespace='accounts')),
    #url(r'^accounts/', include('apps.accounts.urls', namespace='accounts')),
    #url(r'^accounts/profile/', 'home.views.profile', name = 'profile'),
    #url(r'^accounts/signin2/', 'accounts.views.signin', name = 'signin2'),
    #url(r'^accounts/register/', 'apps.accounts.views.register', name = 'register'),
    url(r'^project/', include('apps.project.urls', namespace='project')), 
    #url(r'^projects/$', include('projects.urls')),
    #url(r'^projects/new/$', 'projects.views.new', name = 'new_project'),
    #url(r'^projects/dashboard/$', 'projects.views.dashboard', name = 'dashboard'),
    #url(r'^projects/list/$', 'projects.views.list', name = 'list'),

    url(r'^async/$', 'vendor.django_celery_example.views.test_ftp_download'),
    url(r'^clicks/', 'vendor.click_counter.views.count'), 
    #url(r'^home/', 'home.views.home', name = 'home_page'),
    #url(r'^faq/', 'home.views.faq', name = 'faq'),
    #url(r'^signup/$', 'home.views.signup', name = 'signup'),
    #url(r'^exp/$', 'experiment.views.exp', name = 'exp' ),
    #url(r'^test/$', 'experiment.views.register', name = 'test'),
    #url(r'^base/', 'home.views.base', name = 'base'),

    url(r'^captcha/', include('captcha.urls')), 
    url(r'^admin/', include(admin.site.urls)),
) 

#+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
