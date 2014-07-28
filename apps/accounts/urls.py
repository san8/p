from django.conf.urls import url, patterns 
from django.contrib.auth.decorators import login_required

from .views import ProfileView 


urlpatterns = patterns('',

    url(r'^profile', login_required(ProfileView.as_view()), name='account_profile'),
    #url(r'^editprofile', EditProfile.as_view(), name='account_editprofile'),
    #url(r'^signup', SignUpView.as_view(), name='accounts_signup'),
)
