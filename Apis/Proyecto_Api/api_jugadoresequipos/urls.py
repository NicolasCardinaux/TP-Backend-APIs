from django.urls import path
from api_jugadoresequipos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jugadores_rest/', views.jugadores_rest, name='jugadores_rest'),
    path('add_jugador/', views.add_jugador_view, name='add_jugador'),
    path('equipos_rest/', views.equipos_rest, name='equipos_rest'),
    path('add_equipo/', views.add_equipo_view, name='add_equipo'),
]
