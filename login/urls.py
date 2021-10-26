from django.urls import path
from . import views

urlpatterns = [
#     path('', views.index, name= 'index'),
    path('', views.login_view, name='login'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
]