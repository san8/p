from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .views import (ProfileView, PaymentSuccessView, InsufficientBalanceView,
                    PaymentCancelView)


urlpatterns = patterns(
    '',

    url(r'^profile/$', login_required(ProfileView.as_view()),
        name='account_profile'),
    url(r'^payment-success/$', csrf_exempt(login_required(PaymentSuccessView)),
        name='payment-success'),
    url(r'^payment-cancel/$', login_required(PaymentCancelView),
        name='payment-cancel'),
    url(r'^insufficient-balance/$', login_required(InsufficientBalanceView),
        name='insufficient_balance')

)
