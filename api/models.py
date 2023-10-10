from django.db import models

# Create your models here.

class Task(models.Model):
  id = models.IntegerField(primary_key=True, null=False)
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True, null=True)
  deadline  = models.DateField(blank=True, null=True)
  reminder_time = models.DateTimeField(blank=True, null=True)
  completed = models.BooleanField(default=False, blank=True, null=True)
  priority = models.CharField(max_length=6, blank=False, null=False, default='low')
  # make a sample json object for the above fields
      
  def __str__(self):
    return self.title