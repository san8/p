from django.conf.urls import url, patterns 

urlpatterns = patterns('',

    url(r'^home/', 'home.views.home', name = 'home_page'),
    url(r'^faq/', 'home.views.faq', name = 'faq'),

    url(r'^accounts/profile/', 'home.views.profile', name = 'profile'),
    url(r'^accounts/signin2/', 'accounts.views.signin', name = 'signin2'),
    url(r'^accounts/register/', 'accounts.views.register', name = 'register'),

    #hard coded signup         
    url(r'^signup/$', 'home.views.signup', name = 'signup'),
    #url(r'^exp/$', 'experiment.views.exp', name = 'exp' ),

    #django-registration package    
    #url(r'^accounts/$', include('registration.backends.default.urls') ),

    #test
    #url(r'^test/$', 'experiment.views.register', name = 'test'),
    #url(r'^base/', 'home.views.base', name = 'base'),

    url(r'^$', 'home.views.base', name = 'home'),

    #url(r'^', include('projects.urls')),
    #url(r'^projects/$', include('projects.urls')),
    url(r'^projects/new/$', 'projects.views.new', name = 'new_project'),
    url(r'^projects/dashboard/$', 'projects.views.dashboard', name = 'dashboard'),
    url(r'^projects/list/$', 'projects.views.list', name = 'list'),


    
)
