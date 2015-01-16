import pytz

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.template.response import TemplateResponse

from .models import Customer


class ProfileView(View):
    def get(self, request):
        customer_id = request.user.id
        user = Customer.objects.get(user_id=customer_id)
        return render(request, 'accounts/profile.html',
                      {'timezones': pytz.common_timezones,
                       'user_timezone': user.timezone,
                       'balance': "{0:.2f}".format(user.balance),})

    def post(self, request):
        customer_id = request.user.id
        instance = Customer.objects.get(user_id=customer_id)
        instance.timezone = request.POST['timezone']
        instance.save()
        request.session['django_timezone'] = request.POST['timezone']
        return redirect(reverse("account:account_profile"))


def PaymentSuccessView(request):
    """
    View to show that payment is successful.
    """
    template_name = 'accounts/payment_success.html'
    return TemplateResponse(request, template_name)


def PaymentCancelView(request):
    """
    View to show that payment is cancelled.
    """
    template_name = 'accounts/payment_cancel.html'
    return TemplateResponse(request, template_name)


def InsufficientBalanceView(request):
    """
    View to show insufficient balance.
    """
    template_name = 'accounts/insufficient_balance.html'
    return TemplateResponse(request, template_name)
