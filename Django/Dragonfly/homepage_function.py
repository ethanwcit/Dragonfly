from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.template.response import TemplateResponse

global context
if 'context' not in globals():
    context = {}
def homepage():
    if User.groups.filter(name='Student').exists():
        context["homepage_url"] = 'studenthomepage'
    elif User.groups.filter(name='Teacher').exists():
        context["homepage_url"] = 'teacherhomepage'
    elif User.groups.filter(name='Parent').exists():
        context["homepage_url"] = 'parenthomepage'
    return context