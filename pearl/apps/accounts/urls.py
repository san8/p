from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .views import ProfileView, PaymentSuccessView


urlpatterns = patterns(
    '',

    url(r'^profile/$', login_required(ProfileView.as_view()),
        name='account_profile'),
    url(r'^payment-success/$',
        csrf_exempt(login_required(PaymentSuccessView.as_view())),
        name='payment'),
)
