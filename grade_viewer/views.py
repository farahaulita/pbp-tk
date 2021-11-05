from django.shortcuts import redirect, render
from login.models import Subject
from django.contrib.auth.decorators import login_required
from login.decorators import student_required
from .forms import QuestionForm


@login_required(login_url='login')
@student_required(login_url="/login/",redirect_field_name='<str:username>/student')
def view_grade(request,name):
	name,category = name.split("-")
	name=name.strip()
	category=category.strip()
	student = request.user
	subject = Subject.objects.get(Class=category,Name=name)
	task = subject.task_set.all()
	if request.method == 'POST':
		form = QuestionForm(request.POST or None)
		if form.is_valid():
			form = QuestionForm(request.POST or None)
			return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
	else:
		form = QuestionForm(request.POST or None)
	response={'student':student,'subject':subject,'tasks':task,'form':form}
	return render(request, 'grade_viewer.html',response)