from django.urls import path
from .views import listview, taskview, addtask, addlist, deletetask, updatetask, moredetails

urlpatterns=[
    path('', listview, name='listview'),
    path('tasks/<int:id>/', taskview, name='taskview'),
    path('addtasks/', addtask, name='addtask'),
    path('addlists/', addlist, name='addlist'),
    path('delete/<int:id>/', deletetask ,name="deletetask"),
    path('updatetask/<int:id>/', updatetask ,name="updatetask"),
    path('moredetails/<int:id>/', moredetails ,name="moredetails"),
]