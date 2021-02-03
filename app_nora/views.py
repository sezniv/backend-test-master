from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Menu, Usuario, Pedido,User
from .forms import CrearMenu, CrearPedido, CrearUsuario
import slack
import os
from django.contrib.auth.mixins import LoginRequiredMixin

"""
Se inicializa Slack
"""
client = slack.WebClient(token= '')

# TE REDIRECCIONA AL INICIO
def inicio(request):
    return render(request, 'app_nora/index.html')


class ListarUsuarios(LoginRequiredMixin, ListView):
    """
    Esta clase genera una lista con todos los usuarios creados,
    se le entrega a user_list.html y se crea una tabla
    donde recorremos todos los elementos de usuarios
    """
    model = User
    fields = ['username','password']
    success_url = reverse_lazy('app_nora:listar_usuarios')


class CrearUsuarios(LoginRequiredMixin, CreateView):
    model = User
    fields = ['username','password']
    success_url = reverse_lazy('app_nora:listar_usuarios')


class EliminarUsuario(LoginRequiredMixin, DeleteView):
    """
    Esta clase te permite eliminar cualquier pedido del model Usuario,
    identifica el id y redirige a user_confirm_delete.html, donde se
    debera confirmar la eliminación, en este caso solo hereados username y password.
    """

    model = User
    fields = ['username','password']
    success_url = reverse_lazy('app_nora:listar_usuarios')


class EditarUsuario(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username','password']
    success_url = reverse_lazy('app_nora:listar_usuarios')


class ListarPedido(LoginRequiredMixin, ListView):
    """
    Esta clase genera una lista con todos los pedidos creados,
    se le entrega a pedido_list.html y se crea una tabla
    donde recorremos todos los elementos de pedidos
    """

    model = Pedido
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_pedido')


class CrearPedido(CreateView):
    """
    Esta clase hereda el modelo Pedido el cual es entregado
    a pedido_form.html, genera un formulario con los atributos
    de la clase.
    """

    model = Pedido
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_pedido')


class EliminarPedido(LoginRequiredMixin, DeleteView):
    """
    Esta clase te permite eliminar cualquier pedido del model Pedido,
    identifica el id y redirige a pedido_confirm_delete.html, donde se
    debera confirmar la eliminación
    """

    model = Pedido
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_pedido')


class EditarPedido(LoginRequiredMixin, UpdateView):
    model = Pedido
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_pedido')


# ESTA CLASE LISTA TODA LAS OPCIONES QUE TIENE UN MENU
class ListarMenu(LoginRequiredMixin, ListView):
    """
    Esta clase genera una lista con todos los menus creados,
    se le entrega a menu_list.html y se crea una tabla
    donde recorremos todos los elementos de menu
    """
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_menu')


class CrearMenu(LoginRequiredMixin, CreateView):
    """
    Esta clase hereda el modelo Menu el cual es entregado
    a menu_form.html, genera un formulario con los atributos
    de la clase.
    """
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_menu')


# ESTA CLASE TE PERMITE EDITAR EL MENU DEL DIA COMO TU LO DESEES
class EditarMenu(LoginRequiredMixin, UpdateView):
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_menu')


#ESTA CLASE TE PERMITE ELIMINAR EL MENU Y VOLVER A GENERAR UNO NUEVO
class EliminarMenu(LoginRequiredMixin, DeleteView):
    """
    Esta clase te permite eliminar cualquier pedido del model Menu,
    identifica el id y redirige a menu_confirm_delete.html, donde se
    debera confirmar la eliminación
    """
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('app_nora:listar_menu')



class MenuVistaDetalle(DetailView):
    """
    Esta clase posee una funcion la cual busca en la base de datos por
    el uuid del menu del dia y lo entrega a la pagina_personalizada.html
    esto para manejar un catalogo una vista unica para el usuario.
    """

    template_name = 'app_nora/pagina_personalizada.html'

    def get_object(self):
        id_ = self.kwargs.get("menu_uuid")
        return get_object_or_404(Menu, menu_uuid=id_)


class CreateUsuario(LoginRequiredMixin, CreateView):
    """
    LoginRequiredMixin = Requiere autenticacion
    Esta clase hereda los atributos de la clase Usuario,
    el formulario que utiliza esta clase es user_form.html
    """

    model = Usuario
    fields = '__all__'
    success_url = reverse_lazy('app_nora:crear_usuario')


def enviar_mensaje(request):
    """
    Esta funcion consulta en la base de datos los datos del menu del día
    en formato de diccionario luego se guarda la el campo uuid en la variable key_menu
    y se concatena con la ruta del servidor para ser enviada como ruta en mensaje de Slack
    text envia un texto concatenado con las opciones del día agregando la variable 'ruta'.
    con chat_postMessage generamos un post en Slack, en este caso le enviamos el nombre del canal
    y el texto a enviar, le entregamos la variable text como texto, en caso de ser exitoso retornara 
    mensaje exitoso. 
    """

    query = Menu.objects.all().values()[0]
    key_menu = query['menu_uuid']
    ruta = "http://127.0.0.1:5000/menu/"+str(key_menu)+''
    text = f"""\n     
                    > ¡Hola!
                    > Comparto con ustedes el menú de hoy :)
                    
                    1) Opcion 1: {query['opcion_1']} \n 
                    2) Opcion 2: {query['opcion_2']} \n
                    3) Opcion 3: {query['opcion_3']} \n 
                    4) Opcion 4: {query['opcion_4']} \n
                    
                    ¡Que tengas un buen día! \n
                    Puedes visitar el menu en {ruta} """
                        
    client.chat_postMessage(channel='#cornershop_chile', text=text)
    return render(request, 'app_nora/enviado_exitoso.html')



    

