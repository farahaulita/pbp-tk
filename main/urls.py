from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('success', views.success_page, name='success'),
    path('suggestion_json', views.save_json, name='json')

]
