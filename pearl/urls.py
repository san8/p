from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pearl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^home/', 'home.views.home', name = 'home_page'),
    url(r'^faq/', 'home.views.faq', name = 'faq'),
    url(r'^accounts/profile/', 'home.views.profile', name = 'profile'),

    #hard coded signup
    #url(r'^signup/$', 'home.views.signup', name = 'signup'),

    #django-registration package
    #url(r'^accounts/$', include('registration.backends.default.urls') ),

    #test
    #url(r'^test/$', 'experiment.views.register', name = 'test'),
    #url(r'^base/', 'home.views.base', name = 'base'),

    url(r'^$', 'home.views.base', name = 'home'),
)

