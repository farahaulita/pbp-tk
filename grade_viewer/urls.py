from django.urls import path
from .views import view_grade

urlpatterns = [
    path('', view_grade, name='view_grade'),
]
