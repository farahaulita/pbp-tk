from django.shortcuts import redirect, render
#from django.http import HttpResponseRedirect, HttpResponse
from login.models import User, Task, Subject, Submissions
from django.contrib.auth.decorators import login_required
from login.decorators import student_required
from .forms import QuestionForm

''' 
- Add view_grade function to views.py in main folder and call views.view_grade in urls.py in main folder 
- Add grade_viewer to settings.py
!!!!! PASS SUBJECT FROM VIEWS.PY IN STUDENT DASHBOARD !!!!!
general idea:
- handle multiple form in student dashboard where each button is associated with one subject (student's subject)
- send the subject associated with the button to views on click
- pass object (the subject) from views called from the template to this views
very helpful page: https://stackoverflow.com/questions/41080955/django-passing-object-from-template-to-views
THANKS!
'''

#@login_required(login_url='login')
#@student_required(login_url="/login/",redirect_field_name='<str:username>/student')
#def view_grade(request,subjectname):
def view_grade(request):
	'''
	student = request.user
	subject = request.session.get('subject',None)
	response={'student':student,'subject':subject,'form':form}
	'''
	if request.method == 'POST':
		form = QuestionForm(request.POST or None)
		if form.is_valid():
			form = QuestionForm(request.POST or None)
			return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
	else:
		form = QuestionForm(request.POST or None)
	response={'form':form}
	return render(request, 'grade_viewer.html',response)