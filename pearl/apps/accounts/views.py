from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods
from pytz import common_timezones

from .models import Customer


@login_required
@require_http_methods(['GET', 'POST'])
def account_profile(request):
    """
    profile view for users.
    """
    if request.method == 'GET':
        user = request.user
        customer = Customer.objects.get(user=user)
        return render(request, 'accounts/profile.html',
                      {'timezones': common_timezones,
                       'user_timezone': customer.timezone,
                       'balance': "{0:.2f}".format(customer.balance)})

    if request.method == 'POST':
        user = request.user
        instance = Customer.objects.get(user=user)
        instance.timezone = request.POST['timezone']
        instance.save()
        request.session['django_timezone'] = request.POST['timezone']
        return redirect(reverse("account_profile"))


@login_required
def payment_success_view(request):
    """
    View to show that payment is successful.
    """
    template_name = 'accounts/payment_success.html'
    return TemplateResponse(request, template_name)


@login_required
def payment_cancel_view(request):
    """
    View to show that payment is cancelled.
    """
    template_name = 'accounts/payment_cancel.html'
    return TemplateResponse(request, template_name)


@login_required
def insufficient_balance_view(request):
    """
    View to show insufficient balance.
    """
    template_name = 'accounts/insufficient_balance.html'
    return TemplateResponse(request, template_name)
