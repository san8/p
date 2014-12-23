import pytz

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import TemplateView

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


class PaymentSuccessView(TemplateView):
    """
    View to show that payment is successful.
    """
    template_name = 'accounts/payment_success.html'
