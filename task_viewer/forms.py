from django import forms
from .models import Task


class FileForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['submission']
        widget =  {
            'submission': forms.FileField(attrs={'class': 'form-control'}),
        }
