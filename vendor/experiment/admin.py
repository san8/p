from django.contrib import admin
from .models import ProjectReport, TestFTP 
from .models import Book, Publisher, Author 


admin.site.register(ProjectReport) 
admin.site.register(TestFTP)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)

