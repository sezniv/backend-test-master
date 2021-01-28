from django.shortcuts import render
from .forms import CrearMenu
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Menu
from django.urls import reverse_lazy

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
