from django.db import models

class Jugador(models.Model):
    POSICIONES = [
        ('P', 'Portero'),
        ('DC', 'Defensa central'),
        ('DL', 'Defensa lateral'),
        ('CD', 'Centrocampista defensivo'),
        ('CO', 'Centrocampista ofensivo'),
        ('E', 'Extremo'),
        ('D', 'Delantero')
    ]
    EDAD_CHOICES = [(i, i) for i in range(14, 66)]  
    nombre_apellido = models.CharField(max_length=100)
    posicion = models.CharField(max_length=2, choices=POSICIONES)
    edad = models.IntegerField(choices=EDAD_CHOICES)
    posee_equipo = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_apellido
    


class Equipo(models.Model):
    NOMBRE_REFUERZO_OPCIONES = [
        ('P', 'Portero'),
        ('DC', 'Defensa central'),
        ('DL', 'Defensa lateral'),
        ('CD', 'Centrocampista defensivo'),
        ('CO', 'Centrocampista ofensivo'),
        ('E', 'Extremo'),
        ('D', 'Delantero'),
    ]
    
    nombre = models.CharField(max_length=100)
    refuerzo_requerido = models.CharField(max_length=2, choices=NOMBRE_REFUERZO_OPCIONES)
    salario_estimado = models.IntegerField(help_text="Introduce el salario estimado en euros (€).")
    jugadores = models.ManyToManyField(Jugador, blank=True, limit_choices_to={'posee_equipo': False})

    def __str__(self):
        return self.nombre
