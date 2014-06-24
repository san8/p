from django.db import models
from django.contrib.auth.models import User, UserManager

class CustomUser(User):
    company = models.CharField(max_length=100)

    objects = UserManager()


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username

