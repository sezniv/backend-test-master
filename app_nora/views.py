from django.shortcuts import render

def inicio(request):
    return render(request, 'app_nora/inicio.html')

