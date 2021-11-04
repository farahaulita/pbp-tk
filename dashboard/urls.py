from django.urls import path
from .views import dashboard_student,dashboard_teacher, profile, editprofile
from login.views import logoutUser

urlpatterns = [
    path('<str:username>/student', dashboard_student, ),
    path('<str:username>/teacher', dashboard_teacher),
    path('logout', logoutUser),
    path('<str:username>/profile', profile),
    path('<str:username>/editprofile', editprofile),
    
    

]

