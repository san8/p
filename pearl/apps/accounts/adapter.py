from allauth.account.adapter import DefaultAccountAdapter

from .models import Customer


class CustomAccountAdapter(DefaultAccountAdapter):
    def __init__(self):
        super(CustomAccountAdapter, self).__init__()

    def save_user(self, request, user, form):
        super(CustomAccountAdapter, self).save_user(request, user, form)
        data = form.cleaned_data
        Customer.objects.create(user=user,
                                company=data['institution'],
                                salutation=data['salutation'],
                                phone_number=data['phone_number'])
