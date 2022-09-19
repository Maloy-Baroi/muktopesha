from django import forms
from App_main.models import *


class OfferedToDoTheJobModelForm(forms.ModelForm):
    class Meta:
        model = OfferedToDoTheJobModel
        fields = ['offer_text']



class JobModelForm(forms.ModelForm):
    validate_until = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = JobModel 
        exclude = ['author', 'status']

