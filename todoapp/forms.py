from django import forms
from .models import Tasks, ToDoList

#Create your forms here.

class Tasksform(forms.ModelForm):
    class Meta:
        model= Tasks
        fields= '__all__'

class Todolistform(forms.ModelForm):
    class Meta:
        model= ToDoList
        fields= '__all__'

class Tasksupdate(forms.ModelForm):
    class Meta:
        model= Tasks
        fields= '__all__'
