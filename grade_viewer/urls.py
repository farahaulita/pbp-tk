from django.urls import path
from .views import view_grade
#from dashboard.views import dashboard_student
#from task_viewer.views import view_task
#from TaskManager.views import taskmanager

urlpatterns = [
    #path('<str:subjectname>/grade/', view_grade, name='view_grade'),
    path('', view_grade, name='view_grade'),
    #in grade_viewer.html {{!-- change href to href="{% url 'username:dashboard' %}"--}}
    #path('<str:username>/student/', dashboard_student, name='dashboard'),

    #in grade_viewer.html {{! change href to href="{% url 'taskmanager:username:identitas:tambahan' %}"}}
    #path('taskmanager/<str:name>/<int:identitas>/<str:tambahan>', views.taskmanager, name='taskmanager'),

    #in grade_viewer.html {{! change href to href="{% url 'view_task' %}"}}
    #path('view-task', view_task, name='view_task'),
]
