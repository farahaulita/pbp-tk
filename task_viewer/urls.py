from django.urls import path
from .views import view_task, view_subject_task

urlpatterns = [
    path('view-task', view_task, name='view_task'),
    path('view-subject-task', view_subject_task, name='view_subject_task')
]