from django.urls import path
from .views import dashboard_student, dashboard_teacher, profile, ProfileForm

urlpatterns = [
    path('', dashboard_student, name='dashboard'),
    path('teacher', dashboard_teacher),
    path('profile', profile),
    path('editprofile', ProfileForm),
    
    

]

