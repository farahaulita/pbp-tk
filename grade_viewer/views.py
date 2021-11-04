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
- handle multiple form in student dashboard where each button is associated with one subject (student's subject), see [3]
- send the subject associated with the button to views on click, see [2]
- pass object (the subject) from views called from the template to this views, see [1]
some helpful page:
[1] https://stackoverflow.com/questions/9024160/django-pass-object-from-view-to-next-for-processing
[2] https://stackoverflow.com/questions/17599035/django-how-can-i-call-a-view-function-from-template
[3] https://stackoverflow.com/questions/16067603/passing-objects-from-template-to-view-using-django
THANKS!
'''

#@login_required(login_url='login')
#@student_required(login_url="/login/",redirect_field_name='<str:username>/student')
def view_grade(request):
	'''
	student = request.user
	subject = request.session.get('subject',None)
	if request.method == 'POST':
		form = QuestionForm(request.POST or None)
		if form.is_valid():
			form = QuestionForm(request.POST or None)
			return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
	else:
		form = QuestionForm(request.POST or None)
	response={'student':student,'subject':subject,'form':form}
	return render(request, 'grade_viewer.html',response)
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