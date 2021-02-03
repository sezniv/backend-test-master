"""app_nora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "app_nora"

urlpatterns = [
    path("", views.inicio, name="inicio"),

    #CRUD MENU
    path('listar_menu', views.ListarMenu.as_view(), name="listar_menu"),
    path('crear_menu', views.CrearMenu.as_view(), name="crear_menu"),
    path('<pk>/editar_menu', views.EditarMenu.as_view(), name="editar_menu"),
    path('<pk>/eliminar_menu', views.EliminarMenu.as_view(), name="eliminar_menu"),
    path('menu/<slug:menu_uuid>', views.MenuVistaDetalle.as_view(), name="menu_del_dia"),

    #ENVIA MENSAJE A SLACK A CANAL CORNERSHOP
    path('mensaje_enviado', views.enviar_mensaje, name="enviar_mensaje"),
    
    #CRUD USUARIO
    path('listar_usuarios', views.ListarUsuarios.as_view(), name="listar_usuarios"),
    path('crear_usuarios', views.CrearUsuarios.as_view(), name="crear_usuarios"),
    path('<pk>/editar_usuario', views.EditarUsuario.as_view(), name="editar_usuario"),
    path('<pk>/eliminar_usuario', views.EliminarUsuario.as_view(), name="eliminar_usuario"),
    
    #CRUD PEDIDO
    path('crear_pedido', views.CrearPedido.as_view(), name="crear_pedido"),
    path('listar_pedido', views.ListarPedido.as_view(), name="listar_pedido"),
    path('<pk>/eliminar_pedido', views.EliminarPedido.as_view(), name="eliminar_pedido"),
    path('<pk>/editar_pedido', views.EditarPedido.as_view(), name="editar_pedido"),

]
