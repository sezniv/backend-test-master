from django import forms
from .models import Menu


class CrearMenu(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'