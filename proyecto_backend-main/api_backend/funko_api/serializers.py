from rest_framework import serializers
from funko_api.models import Funko, User

class FunkoSerializers(serializers.ModelSerializer):  # Corregido aquí
    class Meta:
        model = Funko
        fields = '__all__'
