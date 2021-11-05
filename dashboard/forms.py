from django import forms
from .models import Profile



<<<<<<< HEAD
class ProfileForm(forms.Form):

    class Meta:
        model = Profile
        fields = ('name', 'birth_date', 'address', )
        widgets = {'birth_date': forms.DateInput(attrs={'type':'date'}),}
=======
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image','name','birth_date','address']



>>>>>>> 895d920d906c78739bbed892074bd829788cf032
