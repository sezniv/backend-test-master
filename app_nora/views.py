from django.shortcuts import render
from .forms import CrearMenu
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from django.urls import reverse_lazy
from .models import Menu
import requests
import sys
import getopt

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

class UrlMenu(View):

    template_name = 'app_nora/pagina_personalizada.html'
    model = Menu

    def get(self, request):
        id = request.menu.menu_uuid
        lista_menu = list(self.model.objects.filter(self.model.menu_uuid==id).values()[0]
        menu = {'menu': lista_menu}
        return render(request, self.template_name, context=menu)


#SEND SLACK MENSAJE USANDO LA API

def send_slack_message(message):
    payload = '{"text":"%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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',
                            data = payload)

    print(response.txt)

def crear_mensaje_slack(argv):

    message = ' '

    try: opts, args = getopt.getopt(argv, "hm:", ["message="])

    except getopt.GetoptError:
        print('views.py -m <message>')
        sys.exit(2)
    if len(opts) == 0:
        message= "HELLO, WORLD"
    for opt,arg in opts:
        if opt == '-h':
            print('views.py -m <message>')
            sys.exit()
        elif opt in ("-m", "--message"):
            message = arg
        
    send_slack_message(message)

if __name__ == "__crear_mensaje_slack__":
    crear_mensaje_slack(sys.argv[1:])



