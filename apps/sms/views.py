# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .forms import CreateUserForm
from .models import User
#twilio package
from twilio.rest import Client

class Home(TemplateView):
    template_name = 'home.html'


class CreateUserView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'create.html'
    success_url = '/'


class UserView(ListView):
    model = User
    template_name = 'user_show.html'