from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

from registration.backends.default.views import RegistrationView

from pearl.settings.base import MEDIA_URL, MEDIA_ROOT
from apps.home.views import HomeView
from apps.accounts.forms import CustomerForm


admin.autodiscover()
pay_pal = get_integration("pay_pal")

urlpatterns = patterns(
    '',

    url(r'^home/', include('apps.home.urls', namespace='home')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
                      {'next_page': '/home/'}),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=CustomerForm),
                                  name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^account/', include('apps.accounts.urls', namespace='account')),
    url(r'^project/', (include('apps.project.urls', namespace='project'))),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view()),
) + static(MEDIA_URL, document_root = MEDIA_ROOT)
