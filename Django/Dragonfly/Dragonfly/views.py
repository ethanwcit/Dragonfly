from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
def studenthomepage(request, homepage="studenthomepage.html"):
    context ={}
    context["homepage_url"] = 'studenthomepage'
    homepage = "studenthomepage.html"
    return TemplateResponse(request, homepage, context)
def parenthomepage(request):
    context={}
    context["homepage_url"] = 'parenthomepage'
    homepage = "parenthomepage.html"
    return TemplateResponse(request, homepage, context)
def teacherhomepage(request):
    context={}
    context["homepage_url"] = 'teacherhomepage'
    homepage = "teacherhomepage.html"
    return TemplateResponse(request, homepage, context)
def loginpage(request):
    return HttpResponse('loginpage')

