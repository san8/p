from django.conf.urls import url, patterns 

from .views import SignUpView 


urlpatterns = patterns('',
    url(r'^signup', SignUpView.as_view(), name='accounts_signup'),
    #url(r'^signout', )
)
