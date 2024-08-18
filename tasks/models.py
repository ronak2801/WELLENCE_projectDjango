import uuid
from django.db import models
from django.contrib.auth.models import User

def some_function():
    from .forms import TaskForm
    # Use TaskForm here



class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    due_by = models.DateTimeField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    is_urgent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.task} (Priority: {self.get_priority_display()})"
