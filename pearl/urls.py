from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pearl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', 'home.views.home', name = 'home_page'),
    url(r'^base/', 'home.views.base', name = 'base'),
    url(r'^$', 'home.views.base', name = 'base'),
)
