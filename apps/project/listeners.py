from django.db.models.signals import post_save 

from .models import NewProject 
from .tasks import print_hello 

"""
def ftp_handler(*args, **kwargs):
    url_list = ['1', '2'] 
    get_ftp_files.apply_async(kwargs={'project_id': '12', 'url_list': url_list })
post_save.connect(ftp_handler, sender=NewProject)

"""

def print_hello_handler(*args, **kwargs):
    print_hello.apply_async()

post_save.connect(print_hello_handler, sender=NewProject)


