from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponseRedirect
from login.models import User
from .models import Profile
from .forms import ProfileForm


# Create your views here.

@login_required(login_url="/login/")
#@student_required(login_url="/login/",redirect_field_name='<str:username>/student')
def dashboard_student(request,username):

    student = request.user

    if student.is_student:
        return render(request, 'dashboard_student.html', {'user':student.get_username(), 'subjects': student.subjects.all()})
    
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/'+student.get_username()+'/teacher')
        
   

@login_required(login_url="/login/")
#@teacher_required(login_url="/login/",redirect_field_name='<str:username>/teacher')
def dashboard_teacher(request,username):
    
    teacher = request.user

    if teacher.is_teacher:
        return render(request, 'dashboard_teacher.html', {'user':teacher.get_username(), 'subjects': teacher.subjects.all()})

    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/'+teacher.get_username()+'/student')
    


def profile(request,username):
    userprofile = request.user.profile
    response = {'userprofile' : userprofile}
    return render(request, 'profile.html', response)


def editprofile(request,username):
    userrole =  request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST or None)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/'+userrole.get_username()+'/profile')

    else:
        form = ProfileForm()

    response = {'form':form
}

    return render(request, 'profileform.html', response )
