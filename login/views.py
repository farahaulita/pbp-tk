from django.shortcuts import render, redirect
from login.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect

# Create your views here.

# def index(request):
#     # isiLogin = User.objects.all().values()  # TODO Implement this
#     # value = {'login': isiLogin}
#     return render(request, 'index.html')


def login_view(request):
    form = LoginForm(request.POST or None)
    temp = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_student:
                login(request, user)
                return redirect('student')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacher')
        else:
            temp = 'error validating form'
    return render(request, 'login.html', {'form': form, 'temp': temp})

def student(request):
    return render(request,'student.html')   #dashboard msg msg


def teacher(request):
    return render(request,'teacher.html')   #dashboard msgmsrg