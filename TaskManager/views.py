from django.shortcuts import redirect, render
from login.models import User, Task, Subject, Submissions
from django.contrib.auth.decorators import login_required
from .forms import AddTaskForm
# Create your views here.

@login_required(login_url='login')
def taskmanager(request, name):
    elemensekolah = request.user
    subjects = elemensekolah.subjects.all()
    task = {}
    for sub in subjects:
        task[sub.id] = {sub.Name: sub.task_set.all()}
    response = {'user': elemensekolah,
                'subjects': task}
    if elemensekolah.get_username() == name:
        return render(request, 'task_manager.html', response)
    else:
        return redirect("http://127.0.0.1:8000/"+elemensekolah.get_username()+"/taskmanager")

@login_required(login_url='/admin/login/')
def add_task(request, name, identitas):
    form = AddTaskForm()
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            formtemp = form.save(commit=False)
            formtemp.subject = Subject.objects.get(pk=identitas)
            formtemp.save()
            return redirect("http://127.0.0.1:8000/"+request.user.get_username()+"/taskmanager")
    response = {'form':form}
    return render(request, 'AddTask.html', response)



    
        


