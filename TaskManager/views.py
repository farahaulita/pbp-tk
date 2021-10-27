from django.shortcuts import redirect, render
from login.models import User, Task, Subject, Submissions
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def taskmanager(request, name):
    elemensekolah = request.user
    subjects = elemensekolah.subjects.all()
    response = {'user': elemensekolah,
                'subjects': subjects}
    if elemensekolah.get_username() == name:
        return render(request, 'task_manager.html', response)
    else:
        return redirect("http://127.0.0.1:8000/"+elemensekolah.get_username()+"/taskmanager")
        return null
        


