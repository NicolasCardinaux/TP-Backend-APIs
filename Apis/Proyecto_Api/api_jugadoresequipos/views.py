from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect
import json


from api_jugadoresequipos.models import Jugador, Equipo
from api_jugadoresequipos.forms import JugadorForm, EquipoForm
from api_jugadoresequipos.serializers import JugadorSerializer, EquipoSerializer

# Función para obtener todos los jugadores
def get_all_jugadores():
    jugadores = Jugador.objects.all().order_by('id') 
    jugadores_serializer = JugadorSerializer(jugadores, many=True)
    return jugadores_serializer.data

# Vista para renderizar la lista de jugadores en una página HTML
def index(request):
    jugadores = get_all_jugadores()
    equipos = get_all_equipos()  
    return render(request, 'index.html', {'jugadores': jugadores, 'equipos': equipos})


# Vista REST para obtener todos los jugadores en formato JSON
def jugadores_rest(request):
    jugadores = get_all_jugadores()
    return JsonResponse(jugadores, safe=False)

# Vista para agregar un nuevo jugador
def add_jugador_view(request):
    if request.method == 'POST':
        jugador_form = JugadorForm(request.POST)
        if jugador_form.is_valid():
            jugador = jugador_form.save()
            return HttpResponseRedirect('/')
    else:  
        jugador_form = JugadorForm()

    return render(request, 'add_jugador_view.html', {'form': jugador_form})


def get_all_equipos():
    equipos = Equipo.objects.all().order_by('id')
    equipos_serializer = EquipoSerializer(equipos, many=True)
    return equipos_serializer.data

# Vista REST para obtener todos los equipos en formato JSON
def equipos_rest(request):
    equipos = get_all_equipos()
    return JsonResponse(equipos, safe=False)

# Vista para agregar un nuevo equipo
def add_equipo_view(request):
    if request.method == 'POST':
        equipo_form = EquipoForm(request.POST)
        if equipo_form.is_valid():
            equipo = equipo_form.save()

            jugadores_seleccionados = equipo_form.cleaned_data['jugadores']
            
            for jugador in jugadores_seleccionados:
                jugador.posee_equipo = True
                jugador.save()

            return redirect('index')
    else:
        equipo_form = EquipoForm()

    return render(request, 'add_equipo_view.html', {'form': equipo_form})