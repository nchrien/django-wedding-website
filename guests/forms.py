from django import forms
from .models import Party, Guest

class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['contact_email', 'comments']