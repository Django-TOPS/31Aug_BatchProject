from django import forms
from .models import NewUser,notes

class NewUserForm(forms.ModelForm):
    class Meta:
        model=NewUser
        fields='__all__'

class NotesForm(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'