from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from django.urls import reverse_lazy
from .models import Menu
from .forms import CrearMenu
import slack
import os
from pathlib import Path
from dotenv import load_dotenv

def inicio(request):
    return render(request, 'app_nora/index.html')


class ListarMenu(ListView):
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_menu')

class CreateMenu(CreateView):
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_menu')

class EditMenu(UpdateView):
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_menu')

class DeleteMenu(DeleteView):
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_menu')

class MenuDetailView(DetailView):
    template_name = 'app_nora/pagina_personalizada.html'
    #query = Menu.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("menu_uuid")
        return get_object_or_404(Menu, menu_uuid=id_)


#SEND SLACK MENSAJE USANDO LA API

def enviar_mensaje(request):

    query = Menu.objects.all().values()[0]
    key_menu = query['menu_uuid']
    lista = "visita nuestro menu del día en http://127.0.0.1:8000/menu/{}".format(key_menu)
    client = slack.WebClient(token= 'xoxb-1697344368020-1690975857909-Jp5vzd9q4Lj1kf3uSCH4AZED')
    client.chat_postMessage(channel='#test', text=lista)
    return render(request, 'app_nora/enviado_exitoso.html')