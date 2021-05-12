from rest_framework import serializers
from .models import RentForm

class RentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentForm
        fields = ('id','name','surname','address', 'date')