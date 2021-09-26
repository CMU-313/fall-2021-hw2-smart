from django import forms

from .models import Review


class DocumentReviewDetailForm(forms.Form):

    # basic information
    firstName = forms.CharField(label='First name', required=True)
    lastName = forms.CharField(label='First name', required=True)
    gradYear = forms.IntegerField(label='Graduation year', required=True)
    fieldOfStudy = forms.CharField(label='Field of Study', required=True)

    # scales for ratings (1-10)
    gpaScale = forms.IntegerField(label='GPA rating', widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '10', 'id':'gpa_scale'}), required=True)
    techinicalScale = forms.IntegerField(label='Technical skills', widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '10', 'id':'gpa_scale'}), required=True)
    communicationScale = forms.IntegerField(label='Communication skills', widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '10', 'id':'gpa_scale'}), required=True)
    experienceScale = forms.IntegerField(label='Experience', widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '10', 'id':'gpa_scale'}), required=True)
