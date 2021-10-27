from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('<str:name>/taskmanager', views.taskmanager, name='taskmanager'),
]
