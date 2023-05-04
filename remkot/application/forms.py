from django import forms
from django.core.exceptions import ValidationError
from .models import *


class AddClientForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Client
        fields = ['fio', 'phone']
        widgets = {
            'fio': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
        }
