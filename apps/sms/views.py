# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic import TemplateView

#twilio package
from twilio.rest import Client

class Home(TemplateView):
    template_name = 'home.html'