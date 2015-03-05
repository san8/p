from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf.urls.defaults import *  # noqa


def server_error(request, template_name='500.html'):
    """
    500 error handler.

    Templates: `500.html`
    Context: None
    """
    return render_to_response(template_name,
        context_instance = RequestContext(request)
    )


handler500 = server_error
