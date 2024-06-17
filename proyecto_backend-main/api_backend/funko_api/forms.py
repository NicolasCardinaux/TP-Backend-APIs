from django import forms

from funko_api.models import Funko


class FunkoForm(forms.ModelForm):

    name = forms.CharField(label="Nombre",
                           widget=forms.TextInput(attrs={'placeholder': 'Funko name'}))
    number = forms.IntegerField(label="Número",
                              widget=forms.TextInput(attrs={'placeholder': 'Funko number'}))
    collection = forms.CharField(label="Colección",
                                 widget=forms.TextInput(attrs={'placeholder': 'Funko collection'}))

    class Meta:
        model = Funko
        fields = [
            'name',
            'number',
            'collection',
            'is_backlight',
        ]
