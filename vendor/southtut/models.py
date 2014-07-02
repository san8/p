from django.db import models

# Create your models here.

class Knight(models.Model):
    first_name = models.CharField(max_length = 100, default='')
    last_name = models.CharField(max_length = 100, default = '')
    college = models.CharField(max_length = 100, default = '')
    city = models.CharField(max_length = 100, default = '')
