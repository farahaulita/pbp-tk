from django.urls import path
from .views import view_grade

urlpatterns = [
    path('<str:name>/', view_grade, name='grade'),
]
