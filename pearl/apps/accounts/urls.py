from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required

from .views import ProfileView


urlpatterns = patterns(
    '',

    url(r'^profile/$', login_required(ProfileView.as_view()),
        name='account_profile'),
)
