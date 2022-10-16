from django import forms
from . import models
from django.forms import ClearableFileInput,SelectDateWidget


class CreateTask_Teacher(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['TaskName', 'TaskDescription', 'DueDate','Class']
        widgets = {
            'DueDate': SelectDateWidget()
        }
class CreateTask_Student(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['TaskName', 'TaskDescription', 'DueDate' ]
        widgets = {
            'DueDate': SelectDateWidget()
        }


class CreateTask_file(forms.ModelForm):
    class Meta:
            model = models.File
            fields = ['file']
            widgets = {
                'file': ClearableFileInput(attrs={'multiple': True}),
            }