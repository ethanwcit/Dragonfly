from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.db.models import Q
global context
if 'context' not in globals():
    context = {}

def homepage(request):
    user = request.user
    if user.groups.filter(name='Student').exists():
        context["homepage_url"] = 'studenthomepage'
    elif user.groups.filter(name='Teacher').exists():
        context["homepage_url"] = 'teacherhomepage'
    elif user.groups.filter(name='Parent').exists():
        context["homepage_url"] = 'parenthomepage'

def markdone(request, tasks_list,tasks):
    Current_User = request.user
    Student_ID = StudentUser.objects.get(UserID=Current_User)
    for task in tasks:
        if MarkDone.objects.filter(Q(TaskID=task) & Q(StudentID=Student_ID)).exists():
            pass
        else:
            new_done = MarkDone(TaskID=task,StudentID=Student_ID)
            new_done.save()
    done = MarkDone.objects.filter(Q(TaskID__in=tasks_list) & Q(StudentID=Student_ID))
    return done
#decorator to redirect to login page if user is not logged in
@login_required(login_url="accounts:login")
#creates task list webpage
def task_list(request):
    homepage(request)
    Current_User = request.user
    if context["homepage_url"] == 'studenthomepage':
        Student_ID = StudentUser.objects.get(UserID=Current_User)
        Classes2 = StudentInClass.objects.filter(StudentID=Student_ID).values_list('ClassID', flat=True).distinct()
        Classes3 = Classes.objects.filter(id__in = Classes2).values_list('id', flat=True).distinct()
        tasks = Task.objects.filter(Q(Class__in= Classes3) | Q(author=Current_User))
        tasks_list =Task.objects.filter(Q(Class__in= Classes3) | Q(author=Current_User)).values_list('id', flat=True).distinct()
        done = markdone(request, tasks_list, tasks)
        #context["classes"] = Classes2
        #context["classes2"] = Classes3
    elif context["homepage_url"] == "teacherhomepage":
        tasks = Task.objects.filter(author=Current_User)
    else:
        #orders all the tasks by the date set
        tasks = Task.objects.all().order_by('DateSet')
    if not tasks:
        context['emptytask'] = "There are no tasks for you at this moment"

    context['tasks']=tasks
    #returns the task list html template using a dictionary
    return render(request, "tasks/tasks_list.html", context)


#decorator to redirect to login page if user is not logged in
@login_required(login_url="accounts:login")
#creates view for the task detail webpage
def task_detail(request,slug):
    homepage(request)
    task = Task.objects.get(id=slug)
    task_files = File.objects.filter(TaskID_id=slug)
    context['task'] = task
    context['task_files'] = task_files
    return render(request, 'tasks/task_detail.html', context)

#decorator to redirect to login page if user is not logged in
@login_required(login_url="accounts:login")
#creates view for the the create task page
def task_create(request):
    homepage(request)
    user=request.user
    Student=False
    if user.groups.filter(name='Student').exists():
        Student=True
    if request.method == 'POST':
        #gets curren task creation form data
        if Student == True:
            form = forms.CreateTask_Student(request.POST)
        else:
            form = forms.CreateTask_Teacher(request.POST)
        form_file = forms.CreateTask_file(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if form.is_valid() and form_file.is_valid():
            #saves form and returns the instance of the form, not commit to the form
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            for f in files:
                file_instance = File(file=f, TaskID=instance)
                file_instance.save()
            return redirect('task:list')
    else:
        if Student == True:
            form = forms.CreateTask_Student()
        else:
            form = forms.CreateTask_Teacher()
        form_file = forms.CreateTask_file()
    context["form"]=form
    context["form_file"] = form_file
    return render(request, 'tasks/task_create.html', context)

def markasdone(request, slug):
    return redirect('task:list')
