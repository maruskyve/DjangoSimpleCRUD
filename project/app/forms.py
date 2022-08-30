from django import forms
from django.forms import ModelForm
from . import models


class TextsForm(forms.ModelForm):
    class Meta:
        model = models.Texts
        fields = "__all__"


class FilesForm(forms.ModelForm):
    class Meta:
        model = models.Files
        fields = "__all__"
