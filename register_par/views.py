
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Equipos

class ListaEquiposView(ListView):
    model = Equipos
    template_name = 'register_par/lista_equipos.html'

class DetalleEquipoView(DetailView):
    model = Equipos
    template_name = 'register_par/detalle_equipo.html'

def index(request):
    return HttpResponse("Hello, world. You're at the register index.")
