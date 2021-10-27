from django.shortcuts import render, redirect
from login.models import User
# from .forms import LoginForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# def index(request):
#     # isiLogin = User.objects.all().values()  # TODO Implement this
#     # value = {'login': isiLogin}
#     return render(request, 'index.html')


def login_view(request):
    if request.user.is_authenticated:
        # return redirect('landingpage')
        print("belumlogut")
        logout(request)
        pass
    else: 
        # form = LoginForm(request.POST or None)
        # temp = None
        if request.method == 'GET':
            # if form.is_valid():
            username = request.GET.get('username')
            password = request.GET.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_student:
                login(request, user)
                print("masuk stud")
                return redirect(user.get_username()+"/taskmanager")
            elif user is not None and user.is_teacher:
                 login(request, user)
                 return redirect('')
            else:
                messages.info(request, 'Username OR password is incorrect')
                print("salah")
        else:
            print("gbs")

    context ={}
    return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def student(request):
    return render(request,'student.html')   #dashboard msg msg


def teacher(request):
    return render(request,'teacher.html')   #dashboard msgmsrg
