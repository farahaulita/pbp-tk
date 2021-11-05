from django.shortcuts import redirect, render
from login.models import User, Task, Subject, Submissions
from django.contrib.auth.decorators import login_required
from .forms import AddTaskForm
# Create your views here.

@login_required(login_url='login')
def taskmanager(request, name, identitas, tambahan):
    elemensekolah = request.user
    subject = Subject.objects.get(pk=identitas)
    tasks = subject.task_set.all()
    response = {'user': elemensekolah.get_username(),
                'tasks': tasks,
                'subject': subject}
    if elemensekolah.get_username() == name:
        return render(request, 'task_manager.html', response)
    else:
        return redirect("http://127.0.0.1:8000/taskmanager/"+elemensekolah.get_username()+"/"+str(subject.id)+"/"+subject.Name+"-"+subject.Class)

@login_required(login_url='login')
def add_task(request, name, identitas, tambahan):
    form = AddTaskForm()
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            formtemp = form.save(commit=False)
            formtemp.subject = Subject.objects.get(pk=identitas)
            formtemp.murid = request.user
            formtemp.save()
            return redirect("http://127.0.0.1:8000/taskmanager/"+request.user.get_username()+"/"+str(formtemp.subject.id)+"/"+formtemp.subject.Name+"-"+formtemp.subject.Class)
    response = {'form':form}
    return render(request, 'AddTask.html', response)



    
        


