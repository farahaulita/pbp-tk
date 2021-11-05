from django.urls import path
from . import views


app_name = 'login'

urlpatterns = [
#     path('', views.index, name= 'index'),
    path('', views.login_view, name='home'),
    path('logout', views.logoutUser, name='out')
    # path('student/', views.student, name='student'),
    # path('teacher/', views.teacher, name='teacher'),

]