from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import Subject, Task

def view_task(request):
    # tasks = Task.objects.filter(subject__name=request.name)
    # response = {'tasks': tasks}
    return render(request, 'task_viewer.html')

def view_subject_task(request):
    return render(request, 'subject_task_viewer.html')