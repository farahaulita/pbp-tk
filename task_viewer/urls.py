from django.urls import path
from .views import view_task, view_subject_task

urlpatterns = [
    path('view-task/<str:name>/<int:identitas>/<str:tambahan>', view_task, name='view-task'),
    path('view-subject-task/<str:name>/<int:identitas>/<str:tambahan>/<int:id>', view_subject_task, name='view-subject-task'),
]