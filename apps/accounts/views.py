from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render 
from django.views.generic.base import View, TemplateView 

from .forms import SignUpForm, EditProfileForm
from .models import Customer 

"""
class ProfileView(View):
    def get(self, request):
        cust_id = request.session['_auth_user_id']
        return render(request, 'accounts/profile.html', {'customer': Customer.objects.get(id=cust_id), })

"""

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'


class EditProfile(View):
    form_class = EditProfileForm

    def get(self, request):
        cust_id = request.session['_auth_user_id']
        customer = Customer.objects.get(id=cust_id)
        form = EditProfileForm()
        return render(request, 'accounts/editprofile.html', {'form': form },)


class SignUpView(View):
    form_class = SignUpForm 

    def get(self, request):
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form},)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            """
             newUser = User.objects.create_user(
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password = form.cleaned_data['password'],
                    #first_name = form.cleaned_data['first_name'],
                    #last_name = form.cleaned_data['lastname'],)
            """
            return HttpResponseRedirect(reverse('home:home_home'))
        return render(request, 'accounts/signup.html', {'form': form},)

