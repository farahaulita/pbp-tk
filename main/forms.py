from django import forms
from .models import Suggestion

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = "__all__"