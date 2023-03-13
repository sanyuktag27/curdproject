from django import forms
from .models import student,Movie


class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '_all_'

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        field = '_all_'