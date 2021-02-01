from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from .models import Menu, Usuario, Pedido
from .forms import CrearMenu, CrearPedido, CrearUsuario
import slack
import os
from pathlib import Path
from django.contrib.auth.mixins import LoginRequiredMixin

# TE REDIRECCIONA AL INICIO
def inicio(request):
    return render(request, 'app_nora/index.html')





# ESTA FUNCION TE PERMITE GUARDAR UN NUEVO PEDIDO
def nuevo_pedido(request):
    context = {
        'crear_pedido': CrearPedido()
    }
    
    if request.method == 'POST':
        crear_pedido = CrearPedido(request.POST)

        if crear_pedido.is_valid():
            crear_pedido.save()
            return render(request, 'app_nora/nuevo_pedido.html', context)
        
        else:
            context = {
                'crear_pedido:': crear_pedido,
            }
    else:
        context = {
            'crear_pedido': CrearPedido(),
        }
    
    return TemplateResponse(request, 'app_nora/nuevo_pedido.html', context)

# ESTA CLASE LISTA TODA LAS OPCIONES QUE TIENE UN MENU
class ListarMenu(LoginRequiredMixin, ListView):
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_menu')


# ESTA CLASE TE PERMITE CREAR EL MENU DEL DIA CON FECHA DEL DIA Y  UN UUID COMO IDENTIFICADOR
class CreateMenu(LoginRequiredMixin, CreateView):
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_menu')


# ESTA CLASE TE PERMITE EDITAR EL MENU DEL DIA COMO TU LO DESEES
class EditMenu(LoginRequiredMixin, UpdateView):
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_menu')


#ESTA CLASE TE PERMITE ELIMINAR EL MENU Y VOLVER A GENERAR UNO NUEVO
class DeleteMenu(LoginRequiredMixin, DeleteView):
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_menu')


#ESTA CLASE BUSCA EN LA BASE DE DATOS EL UUID DEL DÍA Y LO INSERTA EN EL TEMPLATE DESIGNADO
class MenuDetailView(DetailView):
    template_name = 'app_nora/pagina_personalizada.html'
    #query = Menu.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("menu_uuid")
        return get_object_or_404(Menu, menu_uuid=id_)

class CreateUsuario(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = '__all__'
    success_url = reverse_lazy('app_nora:crear_usuario')


#ESTA FUNCION BUSCA EN LA BASE DE DATOS EL UUID DEL CATALOGO DEL MENU DEL DÍA Y LO CONCATENA CON LA RUTA DEL LOCALHOST PARA
#PARA PODER PASARLO COMO MENSAJE EN LA APP DE SLACK, LE DIGO EN QUE CANAL DEBE POSTER Y QUE DEBE POSTEAR

def enviar_mensaje(request):

    query = Menu.objects.all().values()[0]
    key_menu = query['menu_uuid']
    texto = "visita nuestro menu del día en http://127.0.0.1:8000/menu/"
    text = "{}{}".format(texto,key_menu)
    client = slack.WebClient(token= 'xoxb-1697344368020-1696311666130-hGJWTsjHbztsDmbSMq5t2QW5')
    client.chat_postMessage(channel='#cornershop_chile', text=text)
    return render(request, 'app_nora/enviado_exitoso.html')
