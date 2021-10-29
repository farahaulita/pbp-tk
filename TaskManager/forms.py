from django.forms import ModelForm, widgets
from django import forms
from login.models  import User, Task, Submissions, Subject

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['Name', 'Description', 'deadline']
        widgets = {
            'deadline' : DateTimeInput(),
        }
