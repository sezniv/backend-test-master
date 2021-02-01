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
    path("", views.inicio),
    path('listar_menu', views.ListarMenu.as_view(), name="listar_menu"),
    path('crear_menu', views.CreateMenu.as_view(), name="crear_menu"),
    path('<pk>/editar_menu', views.EditMenu.as_view(), name="editar_menu"),
    path('<pk>/eliminar_menu', views.DeleteMenu.as_view(), name="eliminar_menu"),
    path('menu/<slug:menu_uuid>', views.MenuDetailView.as_view(), name="menu_del_dia"),
    path('mensaje_enviado', views.enviar_mensaje, name="enviar_mensaje"),
    path('nuevo_pedido', views.nuevo_pedido, name="nuevo_pedido"),
    path('crear_usuario', views.CreateUsuario.as_view(), name="crear_usuario"),
]
