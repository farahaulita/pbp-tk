from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponseRedirect
from login.models import User
from .models import Profile
from .forms import ProfileForm
<<<<<<< HEAD
=======
from django.http import JsonResponse
>>>>>>> 895d920d906c78739bbed892074bd829788cf032


# Create your views here.

@login_required(login_url="/login/")
#@student_required(login_url="/login/",redirect_field_name='<str:username>/student')
def dashboard_student(request,username):

    student = request.user
<<<<<<< HEAD

    if student.is_student:
        return render(request, 'dashboard_student.html', {'user':student.get_username(), 'subjects': student.subjects.all()})
    
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/'+student.get_username()+'/teacher')
=======
    #subject = student.subjects.all()
    #tasks = subject.task_set.all()

    if student.is_student:
        return render(request, 'dashboard_student.html', {'profile': student.profile ,'user':student.get_username(), 'subjects': student.subjects.all(), })
    
    else:
        return HttpResponseRedirect('http://pbp-tk-e04.herokuapp.com/dashboard/'+student.get_username()+'/teacher')
>>>>>>> 895d920d906c78739bbed892074bd829788cf032
        
   

@login_required(login_url="/login/")
#@teacher_required(login_url="/login/",redirect_field_name='<str:username>/teacher')
def dashboard_teacher(request,username):
    
    teacher = request.user

    if teacher.is_teacher:
<<<<<<< HEAD
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
=======
        return render(request, 'dashboard_teacher.html', {'profile': teacher.profile,'user':teacher.get_username(), 'subjects': teacher.subjects.all(),})

    else:
        return HttpResponseRedirect('http://pbp-tk-e04.herokuapp.com/dashboard/'+teacher.get_username()+'/student')
    

@login_required(login_url="/login/")
def profile(request,username):
    userprofile = request.user.profile
    response = {'userprofile' : userprofile,'profile': userprofile,'user':request.user.get_username(),}
    return render(request, 'profile.html', response)
    
    
@login_required(login_url="/login/")
def editprofile(request,username):
    userrole =  request.user
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST or None,request.FILES or None, instance=request.user.profile)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            custom_form =form.save(False)
            custom_form.user = userrole
            custom_form.save()
            # ...
            # redirect to a new URL:
           
            return HttpResponseRedirect('http://pbp-tk-e04.herokuapp.com/dashboard/'+userrole.get_username()+'/profile')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileForm()
        


    response = {'form':form , 'profile': userrole.profile,'user':userrole.get_username(),}
>>>>>>> 895d920d906c78739bbed892074bd829788cf032

    return render(request, 'profileform.html', response )
