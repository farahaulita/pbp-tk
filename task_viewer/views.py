from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from login.models import Subject, Task, Submissions
from django.contrib.auth.decorators import login_required
from .forms import FileForm
import datetime


@login_required(login_url='/login/')
def view_task(request, name, identitas, tambahan):
    pengguna = request.user
    subject = Subject.objects.get(pk=identitas)
    tasks = subject.task_set.all()
    response = {'user': pengguna.get_username(),
                'tasks': tasks,
                'subject': subject}
    if pengguna.get_username() == name:
        return render(request, 'task_viewer.html', response)
    else:
        return redirect("/task-viewer/view-task/" + pengguna.get_username() + "/" + str(subject.id) + "/" + subject.Name + "-" + subject.Class)

@login_required(login_url='/login/')
def view_subject_task(request, name, identitas, tambahan, id):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            saved = form.save(commit=False)
            saved.task = Task.objects.get(pk=id)
            saved.murid = request.user
            saved.NamaMurid = request.user.get_username()
            saved.save()

            if saved.date > saved.task.deadline:
                saved.ontime = False

            saved.save()
            return redirect('/task-viewer/view-task/' + request.user.get_username() + "/" + str(identitas) + "/" + tambahan)

    else:
        tugas = Task.objects.get(pk=id)
        form = FileForm()
        return render(request, 'subject_task_viewer.html', {'form': form, 'tugas': tugas})
