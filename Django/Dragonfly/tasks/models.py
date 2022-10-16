from django.db import models
from django import forms
from django.contrib.auth.models import User
import os
# Create your models here.

class Task(models.Model):
    TaskName = models.CharField(max_length=500)
    TaskDescription = models.TextField()
    DueDate = models.DateField(auto_now=False, auto_now_add=False)
    DateSet = models.DateTimeField(auto_now_add=True)
    DateModified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Class = models.ForeignKey('tasks.Classes', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.TaskName
    def snippet(self):
        if len(self.TaskDescription) > 50:
            return self.TaskDescription[:50] + "..."
        else:
            return self.TaskDescription



class Comment(models.Model):
    CommentContents = models.TextField()
    PUBLIC = 'Pu'
    PRIVATE = 'Pr'
    PublicOrPrivate = [(PUBLIC, 'Public'),(PRIVATE, 'Private')]
    PubOrPriv = models.CharField(max_length = 2, choices = PublicOrPrivate, default = PRIVATE)
    Task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.CommentContents


class File(models.Model):
    FileName = models.CharField(max_length=500, blank=True, null=True)
    file = models.FileField(blank=True, null=True, upload_to='media/')
    TaskID = models.ForeignKey('tasks.Task', on_delete=models.CASCADE,default=None)


class Classes(models.Model):
    ClassName = models.CharField(max_length=100,null=False)
    def __str__(self):
        return str(self.id)

class Form(models.Model):
    FormName = models.CharField(max_length=100,blank=True, null=True)
    FormYear = models.CharField(max_length=100,blank=True, null=True)
    def __str__(self):
        return self.FormName


class StudentUser(models.Model):
    UserID = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    Form = models.ForeignKey('tasks.Form', on_delete=models.CASCADE, default=None,blank=True)
    def __str__(self):
        return str((self.UserID))



class StudentInClass(models.Model):
    ClassID = models.ForeignKey('tasks.Classes', on_delete=models.CASCADE, null=True)
    StudentID = models.ForeignKey(StudentUser,on_delete=models.CASCADE, default=None)
    def __str__(self):
        return (str(self.ClassID) + " - " + str(self.StudentID))

class MarkDone(models.Model):
    StudentID = models.ForeignKey(StudentUser, on_delete=models.CASCADE, default=None)
    TaskID = models.ForeignKey('tasks.Task', on_delete=models.CASCADE,default=None)
    YES = 'Completed'
    NO = 'Mark As Done'
    Done = models.CharField(max_length=500,choices =[(YES, 'Completed'),(NO, 'Mark As Done')], default = NO)
    def __str__(self):
        return (str(self.TaskID) + " - " + str(self.StudentID) + " - " + str(self.Done))