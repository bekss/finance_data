from django import forms
from .models import Url_File, ReceivedFile


class UrlForms(forms.ModelForm):
    class Meta:
        model = Url_File
        fields = ['url_file']


class ReceivedForms(forms.ModelForm):
    class Meta:
        model = ReceivedFile
        fields = ['url_file']
