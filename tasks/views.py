from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib.auth.views import LogoutView
from django.http import JsonResponse
from django.utils import timezone
from django.db import models
import datetime
from .models import Task
from .forms import TaskForm, CustomUserCreationForm

def some_function():
    from .models import Task 
    
# Combined Registration and Login View
def register_login_combined(request):
    login_form = AuthenticationForm()
    register_form = CustomUserCreationForm()

    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = authenticate(username=login_form.cleaned_data.get('username'),
                                    password=login_form.cleaned_data.get('password'))
                if user is not None:
                    auth_login(request, user)  # Use auth_login to avoid conflict
                    return redirect('landing_page')
        elif 'register' in request.POST:
            register_form = CustomUserCreationForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                return redirect('register_login')

    context = {
        'login_form': login_form,
        'register_form': register_form,
    }
    return render(request, 'tasks/register_login_combined.html', context)

# Landing Page View
def landing_page(request):
    return render(request, 'tasks/landing_page.html')

# Custom Logout View
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# Dashboard View
@login_required
def user_dashboard(request):
    now = timezone.now()
    next_30_days = now + datetime.timedelta(days=30)

    tasks_due_soon = Task.objects.filter(user=request.user, due_by__range=[now, next_30_days]).order_by('due_by')
    urgent_tasks = tasks_due_soon.filter(is_urgent=True)
    task_count = urgent_tasks.count()
    tasks_by_priority = tasks_due_soon.values('priority').annotate(count=models.Count('priority'))

    context = {
        'task_count': task_count,
        'tasks_by_priority': tasks_by_priority,
        'tasks_due_soon': tasks_due_soon,
        'all_tasks': Task.objects.filter(user=request.user).order_by('-created_at'),
    }
    return render(request, 'tasks/user_dashboard.html', context)

# Add Task View 
@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'id': task.id,
                    'task': task.task,
                    'due_by': task.due_by.strftime('%b %d, %Y, %I:%M %p'), 
                    'priority': task.get_priority_display(),
                    'is_urgent': 'Yes' if task.is_urgent else 'No'
                })
            return redirect('user_dashboard')
    else:
        form = TaskForm()

    context = {'form': form}
    return render(request, 'tasks/add_task.html', context)

# Edit Task View
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('user_dashboard')
    else:
        form = TaskForm(instance=task)

    context = {'form': form, 'task': task}
    return render(request, 'tasks/edit_task.html', context)

# Delete Task View
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# Data View for Dashboard
@login_required
def tasks_data(request):
    now = timezone.now()
    next_30_days = now + datetime.timedelta(days=30)

    tasks_due_soon = Task.objects.filter(user=request.user, due_by__range=[now, next_30_days])
    tasks_by_priority = tasks_due_soon.values('priority').annotate(count=models.Count('priority'))
    urgent_tasks_count = tasks_due_soon.filter(is_urgent=True).count()
    line_chart_data = tasks_due_soon.annotate(day=models.functions.TruncDay('due_by')).values('day').annotate(count=models.Count('id')).order_by('day')

    return JsonResponse({
        'tasks_by_priority': list(tasks_by_priority),
        'urgent_tasks_count': urgent_tasks_count,
        'line_chart_data': list(line_chart_data),
    })
