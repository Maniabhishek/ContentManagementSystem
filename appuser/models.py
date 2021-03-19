from django.db import models
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
# from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class Profile(models.Model):
    user_author = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=True, blank=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(
#             user_author=instance)
