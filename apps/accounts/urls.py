from django.conf.urls import url, patterns 
from django.contrib.auth.decorators import login_required


from .views import SignUpView, ProfileView, EditProfile 


urlpatterns = patterns('',

    #url(r'^signup', SignUpView.as_view(), name='accounts_signup'),
    url(r'^profile', login_required(ProfileView.as_view()), name='account_profile'),
    #url(r'^editprofile', EditProfile.as_view(), name='account_editprofile'),
)
