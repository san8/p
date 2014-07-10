from django.db import models
from django.db.models.signals import m2m_changed 

from .forms import MessageForm

a = MessageForm() 

class Abcd():
    pass 


class ProjectReport(models.Model):
    name = models.CharField(max_length=10, default='')

    def __unicode__(self):
        return self.name 


class TestFTP(models.Model):
    name = models.CharField(max_length=10, default='')
    file_address = models.FileField(upload_to='files/')
    url = models.URLField(max_length=100)

    def __unicode__(self):
        return self.name 


class Topping(models.Model):
    pass


class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)


def toppings_changed(sender, **kwargs):
    pass 


m2m_changed.connect(toppings_changed, sender=Pizza.toppings.through)





# Django advanced models 
# http://www.djangobook.com/en/2.0/chapter10.html
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title



