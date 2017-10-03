# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=10,blank=True)
    smstoken = models.CharField(max_length=5,blank=True)



class Sendedsms(models.Model):
    to = models.ForeignKey(User)
    messaje = models.CharField(max_length=40,blank=True)
    created = models.DateTimeField(auto_now_add=True)

