from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from registration.backends.default.views import RegistrationView 

from apps.home.views import HomeView 
from apps.accounts.forms import CustomerForm 

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', HomeView.as_view()),
    url(r'^home/', include('apps.home.urls', namespace='home')),
    url(r'^account/', include('apps.accounts.urls', namespace='account')),
    url(r'^accounts/register/$',  RegistrationView.as_view(form_class=CustomerForm), 
                                  name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^project/', (include('apps.project.urls', namespace='project'))), 
    url(r'^captcha/', include('captcha.urls')), 
    url(r'^admin/', include(admin.site.urls)),

) 
'''

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT })
)

'''
#+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
