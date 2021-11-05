from django.urls import path
from . import views

<<<<<<< HEAD
urlpatterns = [
#     path('', views.index, name= 'index'),
    path('', views.login_view, name='login'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
=======

app_name = 'login'

urlpatterns = [
#     path('', views.index, name= 'index'),
    path('', views.login_view, name='home'),
    path('logout', views.logoutUser, name='out')
    # path('student/', views.student, name='student'),
    # path('teacher/', views.teacher, name='teacher'),
>>>>>>> 895d920d906c78739bbed892074bd829788cf032

]