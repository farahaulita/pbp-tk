from django import forms
from login.models import Submissions


class FileForm(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = ['file', 'comment']
      