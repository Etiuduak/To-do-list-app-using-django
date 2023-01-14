from django.db import models
from django.utils import timezone

# Create your models here.

def one_week_from_now():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title=models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.title

class Tasks(models.Model):
    task=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    datecreated=models.DateTimeField(auto_now_add=True)
    datedue=models.DateTimeField(default=one_week_from_now)
    todo_list=models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.task}: due {self.datedue}'
    class Meta:
        ordering=['datedue']
