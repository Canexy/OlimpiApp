
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('equipos/', views.ListaEquiposView.as_view(), name='lista_equipos'),
]
