from django import forms
from django.forms import fields
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title","content","note_image","source"]