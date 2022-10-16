from django.contrib import admin
from .models import *
from django.apps import apps
admin.site.register(apps.all_models['tasks'].values())