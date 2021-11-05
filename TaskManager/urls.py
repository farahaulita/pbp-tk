from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('taskmanager/<str:name>/<int:identitas>/<str:tambahan>', views.taskmanager, name='taskmanager'),
    path('taskmanager/<str:name>/<int:identitas>/<str:tambahan>/addtask', views.add_task,name='add_task',),
    path('taskmanager/<str:name>/<int:subjectid>/<str:tambahan>/<int:identitas>/edittask', views.edit_task,name='edit_task',),
    path('taskmanager/<str:name>/<int:subjectid>/<str:tambahan>/<int:identitas>/deletetask', views.deletetask, name="delete_task"),
    path('taskmanager/<str:name>/<int:subjectid>/<str:tambahan>/<int:identitas>/submissions', views.viewsubmissions, name="grade_task"),
    path('taskmanager/<str:name>/<int:subjectid>/<str:tambahan>/<int:identitas>/submissions/<int:idfile>/grader', views.grader, name="grade_task")
]
