from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your suggestions or critics'}),label="")