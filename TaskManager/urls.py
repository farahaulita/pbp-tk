from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('taskmanager/<str:name>/<int:identitas>/<str:tambahan>', views.taskmanager, name='taskmanager'),
    path('taskmanager/<str:name>/<int:identitas>/<str:tambahan>/addtask', views.add_task,name='add_task',)
]
