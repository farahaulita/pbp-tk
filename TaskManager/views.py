from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from login.models import User, Task, Subject, Submissions
from django.contrib.auth.decorators import login_required
from .forms import AddTaskForm, GraderForm
# Create your views here.

@login_required(login_url='/login/')
def taskmanager(request, name, identitas, tambahan):
    elemensekolah = request.user
    subject = Subject.objects.get(pk=identitas)
    tasks = subject.task_set.all()
    response = {'user': elemensekolah.get_username(),
                'tasks': tasks,
                'subject': subject}
    if elemensekolah.get_username() == name:
        return render(request, 'cardextend.html', response)
    else:
        return redirect("/taskmanager/"+elemensekolah.get_username()+"/"+str(subject.id)+"/"+subject.Name+"-"+subject.Class)

@login_required(login_url='/login/')
def add_task(request, name, identitas, tambahan):
    form = AddTaskForm()
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            formtemp = form.save(commit=False)
            formtemp.subject = Subject.objects.get(pk=identitas)
            formtemp.save()
            return redirect("/taskmanager/"+request.user.get_username()+"/"+str(formtemp.subject.id)+"/"+formtemp.subject.Name+"-"+formtemp.subject.Class)
    response = {'form':form}
    return render(request, 'AddTask3.0.html', response)

@login_required(login_url='/login/')
def edit_task(request, name, subjectid, identitas, tambahan):
    form = Task.objects.get(pk=identitas)
    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=form)
        if form.is_valid():
            model = form.save()
            return redirect("/taskmanager/"+request.user.get_username()+"/"+str(model.subject.id)+"/"+model.subject.Name+"-"+model.subject.Class)
    response = {'form':form}
    return render(request, 'frontview.html', response)

@login_required(login_url='/login/')
def deletetask(request, name, subjectid, identitas, tambahan):
    model = Task.objects.get(pk=identitas)
    model.delete()
    data = dict()
    subject= Subject.objects.get(pk=subjectid);
    tasks = subject.task_set.all()
    data['html_task_list'] = render_to_string('cardinclude.html', {
        "tasks": tasks
    })
    return JsonResponse(data)


@login_required(login_url='/login/')
def viewsubmissions(request, name, subjectid, identitas, tambahan):
    task = Task.objects.get(pk=identitas)
    submissions = task.submissions_set.all()
    response = {
        'task': task,
        'submissions': submissions,
    }
    return render(request, 'view_submissions.html', response)

def grader(request, name,subjectid, identitas, tambahan, idfile):
    form = Submissions.objects.get(pk=idfile)
    if request.method == 'POST':
        form = GraderForm(request.POST, instance=form)
        if form.is_valid():
            form.save()
            return redirect("/taskmanager/"+request.user.get_username()+"/"+str(subjectid)+"/"+tambahan+"/"+str(identitas)+"/"+"submissions")
    response = {'form':form}
    return render(request, 'grader.html', response)


    
        


