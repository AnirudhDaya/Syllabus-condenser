from django import forms
from .models import *

class UploadQuestions(forms.ModelForm):
    class Meta:
        model = questions
        fields = ('title', 'pdf',)