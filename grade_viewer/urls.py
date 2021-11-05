from django.urls import path
from .views import view_grade
from dashboard.views import dashboard_student

urlpatterns = [
    path('grade/<str:name>/', view_grade, name='grade'),
    path('<str:username>/student/', dashboard_student, name='dashboard'),
]
