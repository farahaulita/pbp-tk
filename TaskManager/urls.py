from django.urls import path

from . import views

urlpatterns = [
    path('<str:name>/<int:identitas>/<str:tambahan>', views.taskmanager, name='taskmanager'),
    path('<str:name>/<int:identitas>/<str:tambahan>/addtask', views.add_task,name='add_task',),
    path('<str:name>/<int:subjectid>/<str:tambahan>/<int:identitas>/edittask', views.edit_task,name='edit_task',),
    path('<str:name>/<int:subjectid>/<str:tambahan>/<int:identitas>/deletetask', views.deletetask, name="delete_task"),
    path('<str:name>/<int:subjectid>/<str:tambahan>/<int:identitas>/submissions', views.viewsubmissions, name="grade_task"),
    path('<str:name>/<int:subjectid>/<str:tambahan>/<int:identitas>/submissions/<int:idfile>/grader', views.grader, name="grade_task")
]
