# -*- coding: utf-8 -*-

# third party imports
from django.conf.urls import url, patterns
from django.views.decorators.csrf import csrf_exempt

# pearl imports
from . import views


urlpatterns = patterns(
    '',

    url(r'^payment-success/$', csrf_exempt(views.payment_success_view),
        name='payment-success'),
    url(r'^payment-cancel/$', views.payment_cancel_view,
        name='payment-cancel'),
    url(r'^insufficient-balance/$', views.insufficient_balance_view,
        name='insufficient_balance'),
    url(r'^validate_recaptcha/(?P<response_token>\w+)', views.validate_recaptcha,
        name='validate_recaptcha')
)
