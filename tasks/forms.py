# tasks/forms.py

from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'due_by', 'priority', 'is_urgent']

