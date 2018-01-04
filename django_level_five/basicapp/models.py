from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    # Create relationship between user and User(user dont inherit from  User)
    user = models.OneToOneField(User)

    # Add new fields/attributes

    portfolio_site = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
