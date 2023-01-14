from django.contrib import messages
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import ToDoList, Tasks
from .forms import Tasksform, Todolistform, Tasksupdate

# Create your views here.

def listview(request):
    lists=ToDoList.objects.all()
    return render(request, 'todoapp/listview.html', {'lists':lists})

def taskview(request, id):
    todo_lists=ToDoList.objects.get(pk=id)
    tasks=Tasks.objects.filter(todo_list=todo_lists)
    return render(request, 'todoapp/taskview.html', {'tasks':tasks})

def addtask(request):
    if request.method=='POST':
        form= Tasksform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form= Tasksform(request.POST)
    return render(request, 'todoapp/addtask.html', {'addtaskform':form})

def addlist(request):
    if request.method=='POST':
        form= Todolistform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form= Todolistform(request.POST)
    return render(request, 'todoapp/addlist.html', {'addlistform':form})

def deletetask(request,id):
    delpost=Tasks.objects.get(pk=id)
    delid=delpost.id
    if request.method=="POST":
        delpost.delete()
        messages.info(request, "Your task has been deleted successfully")
        return redirect("/")
    else:
        return render(request, "todoapp/deletetask.html", {"delid":delid})

def updatetask(request, id):
    tasks=Tasks.objects.get(pk=id)
    if request.method=="POST":
        form = Tasksupdate(request.POST, request.FILES, instance=tasks)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form= Tasksupdate(instance=tasks)
    return render(request, 'todoapp/updatetask.html', {'updatetaskform':form})

def moredetails(request, id):
    details=Tasks.objects.get(pk=id)
    return render(request, 'todoapp/moredetails.html', {'details':details})