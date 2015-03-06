from billing import get_integration
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from pearl.settings.base import MEDIA_URL, MEDIA_ROOT
from apps.home.views import HomeView, ErrorView
from apps.accounts.views import account_profile


admin.autodiscover()
pay_pal = get_integration("pay_pal")

urlpatterns = patterns(
    '',

    url(r'^500/$', 'django.views.defaults.server_error'),
    url(r'^paypal-ipn-handler/', include(pay_pal.urls)),
    url(r'^home/', include('apps.home.urls', namespace='home')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/home/'}),
    url(r'^account/', include('apps.accounts.urls', namespace='account')),
    url(r'^accounts/profile/$', login_required(account_profile),
        name='account_profile'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^project/', (include('apps.project.urls', namespace='project'))),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view()),
) + static(MEDIA_URL, document_root=MEDIA_ROOT)
