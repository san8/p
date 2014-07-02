from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response, render 
from django.views.generic.base import View

from .forms import SignUpForm 


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

"""
class SignupView(View):
    form_class = UserProfileForm 
    second_form_class = UserForm 

    def get(self, request):
        user_form = UserProfileForm()
        user_profile_form = UserForm 
        return render(request, 'accounts/signup.html', {'user_form': user_form, 'user_profile_form': user_profile_form},)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home_page'))
        return render('accounts/signup.html', {'form': form},)



def signin(request):
    username = request.POST.get['username']
    password = request.POST.get['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('projects.views.dashboard'))
        else:
            return HttpResponseRedirect(reverse('accounts.views.disabled'))
    else:
        return HttpResponseRedirect(reverse('accounts.views.invalid'))


def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm
        profile_form = UserProfileForm

    return render_to_response(
            'accounts/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered },
            context)

            
def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponse('/rango/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details."
            return HttpResponse("Invaled details.")
    else:
        return render_to_response('rango/login.html', context)



def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('rango/login.html', {}, context)

"""

