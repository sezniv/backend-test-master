from django import forms
from .models import *
from django.contrib.auth.models import User

class CrearMenu(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

class CrearPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class CrearUsuario(forms.ModelForm):
    class Meta:
        model: Usuario
        fields = '__all__'