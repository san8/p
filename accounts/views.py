from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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

