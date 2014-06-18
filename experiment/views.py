from django.shortcuts import render
from forms import MessageForm
 
def exp(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'exp.html', {'form': MessageForm()})
