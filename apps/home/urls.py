from django.conf.urls import url, patterns 

from .views import HomeView, FAQView


urlpatterns = patterns('',

    url(r'^faq/$', FAQView.as_view(), name = 'home_faq'),
    url(r'^$', HomeView.as_view(), name = 'home_home'),

    #url(r'^', include('projects.urls')),
    #url(r'^$', 'home.views.base', name = 'home'),
    #url(r'^projects/$', include('projects.urls')),
    #url(r'^faq/', 'home.views.faq', name = 'faq'),
    #url(r'^base/', 'home.views.base', name = 'base'),
    #url(r'^exp/$', 'experiment.views.exp', name = 'exp' ),
    #url(r'^signup/$', SignupView.as_view(), name = 'signup'),
    #url(r'^test/$', 'experiment.views.register', name = 'test'),
    #url(r'^accounts/profile/', 'home.views.profile', name = 'profile'),
    #url(r'^accounts/signin2/', 'accounts.views.signin', name = 'signin2'),
    #url(r'^accounts/register/', 'accounts.views.register', name = 'register'),
    #url(r'^signup/$', 'home.views.signup', name = 'signup'),
    #url(r'^accounts/$', include('registration.backends.default.urls') ),
    #url(r'^projects/new/$', 'projects.views.new', name = 'new_project'),
    #url(r'^projects/dashboard/$', 'projects.views.dashboard', name = 'dashboard'),
    #url(r'^projects/list/$', 'projects.views.list', name = 'list'),

)



