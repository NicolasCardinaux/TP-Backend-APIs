from django import forms
from api_jugadoresequipos.models import Jugador, Equipo

class JugadorForm(forms.ModelForm):
    nombre_apellido = forms.CharField(label="Nombre y Apellido",
                                      widget=forms.TextInput(attrs={'placeholder': 'Nombre y Apellido '}))
    posicion = forms.ChoiceField(label="Posición", choices=Jugador.POSICIONES,
                                 widget=forms.Select())
    edad = forms.ChoiceField(label="Edad", choices=Jugador.EDAD_CHOICES,
                             widget=forms.Select())
    posee_equipo = forms.BooleanField(label="Posee Equipo", required=False)

    class Meta:
        model = Jugador
        fields = [
            'nombre_apellido',
            'posicion',
            'edad',
            'posee_equipo',
        ]


class EquipoForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre del Equipo",
                             widget=forms.TextInput(attrs={'placeholder': 'Nombre del Equipo'}))
    refuerzo_requerido = forms.ChoiceField(label="Refuerzo Requerido", choices=Equipo.NOMBRE_REFUERZO_OPCIONES,
                                           widget=forms.Select())
    salario_estimado = forms.IntegerField(label="Salario Estimado",
                                          widget=forms.NumberInput(attrs={'placeholder': 'Salario Estimado'}))
    jugadores = forms.ModelMultipleChoiceField(
        queryset=Jugador.objects.filter(posee_equipo=False),  # Filtrar jugadores con posee_equipo en False
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

    class Meta:
        model = Equipo
        fields = ['nombre', 'refuerzo_requerido', 'salario_estimado', 'jugadores']

    def __init__(self, *args, **kwargs):
        super(EquipoForm, self).__init__(*args, **kwargs)
        if 'refuerzo_requerido' in self.data:
            refuerzo_requerido = self.data.get('refuerzo_requerido')
            self.fields['jugadores'].queryset = Jugador.objects.filter(posicion=refuerzo_requerido, posee_equipo=False)

        # Modificar cómo se muestran las etiquetas de los jugadores
        self.fields['jugadores'].label_from_instance = lambda obj: f"{obj.nombre_apellido} ({obj.get_posicion_display()})"
