from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
# Create your views here.

global context
if 'context' not in globals():
    context = {}

def login_view(request, homepage="base_layout.html"):
    #checks if user has sent a POST request
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        #checks if credentials are valid
        if form.is_valid():
        #gets the type of user
            user = form.get_user()
            login(request, user)
        #checks if a "next" value exists
            if 'next' in request.POST:
                #redirects user back to previous page
                return redirect(request.POT.get('next'))
            else:
                    # checks if the User is a student
                if user.groups.filter(name='Student').exists():
                    context["homepage_url"] = 'studenthomepage'
                    homepage  = "studenthomepage.html"
                    return TemplateResponse(request, homepage, context)
                elif user.groups.filter(name='Teacher').exists():
                    context["homepage_url"]  = 'teacherhomepage'
                    homepage  = "teacherhomepage.html"
                    return TemplateResponse(request, homepage, context)
                elif user.groups.filter(name='Admin').exists():
                    return redirect('admin/')
                elif user.groups.filter(name='Parent').exists():
                    context["homepage_url"]  = 'parenthomepage'
                    homepage  = "parenthomepage.html"
                    return TemplateResponse(request, homepage, context)

    else:
     form = AuthenticationForm()
     #if no post request sent the form is a blank login form
    return render(request,'accounts/login.html', {'form': form})

def logout_view(request):
 if request.method == 'POST':
     logout(request)

 return redirect('accounts:login')

