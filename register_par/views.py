
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Equipos

class ListaEquiposView(ListView):
    model = Equipos
    template_name = 'register_par/equipos.html'

def index(request):
    return HttpResponse("Hello, world. You're at the register index.")
