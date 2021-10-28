from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from login.decorators import student_required


# Create your views here.

def dashboard_student(request):
    return render(request, 'dashboard_student.html')


def dashboard_teacher(request):
    return render(request, 'dashboard_teacher.html')


def profile(request):
    pass


def ProfileForm(request):
    pass