from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .forms import QuestionForm

''' 
- Add view_grade function to views.py in main folder and call views.view_grade in urls.py in main folder 
- Add grade_viewer to settings.py
'''

def view_grade(request):
	message = request.POST.get('message',False)
	if request.method == 'POST':
		form = QuestionForm(request.POST or None)
		if form.is_valid():
			return HttpResponseRedirect(".")
	else:
		form = QuestionForm(request.POST or None)
	template = loader.get_template('grade_viewer.html')
	return HttpResponse(template.render({'form':form}, request))