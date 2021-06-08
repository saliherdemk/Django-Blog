from django import forms
from django.forms import fields
from .models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ["piece","composer","picture","audio"]