from django import forms
from .models import Profile



class ProfileForm(forms.Form):

    class Meta:
        model = Profile
        fields = ('name', 'birth_date', 'address', )
        widgets = {'birth_date': forms.DateInput(attrs={'type':'date'}),}