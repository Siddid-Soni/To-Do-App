from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    reminder_time = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    priority = models.CharField(max_length=6, blank=False, null=False, default='low')

    # make a sample json object for the above fields

    def __str__(self):
        return self.title
