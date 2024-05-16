from django import forms
from voyage.models import FormContact

class FormContactAjout(forms.ModelForm):
    class Meta:
        model = FormContact
        exclude = ['Status','dateCreate']
