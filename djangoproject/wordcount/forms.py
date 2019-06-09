from django import forms
from .models import Fulltext

class FulltextForm(forms.ModelForm):
    class Meta:
        model = Fulltext
        fields = ['text']