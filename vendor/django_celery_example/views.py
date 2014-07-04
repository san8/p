"""
from django.views.decorators.csrf import csrf_exempt 
from django.http import HttpResponse 

from .forms import RegistrationForm 
#from .utilities import create_user 
from .tasks import add_to_count 

import subprocess 


@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
        #create_user(form.cleaned_data)
            return HttpResponse('success')


def test_async(request):
    add_to_count.delay()
    return HttpResponse('Your async request is processing.')


def test_ftp_download(request):
    out = subprocess.check_output(['wget', 'http://www.avilpage.com/'])
    return HttpResponse(out.text)
"""

def test_ftp_download(request):
    pass 
