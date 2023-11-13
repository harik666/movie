from django import forms
from .models import Movies


class FormMovie(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'des', 'year', 'img']
