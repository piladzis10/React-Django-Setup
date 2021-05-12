from django.shortcuts import render
from rest_framework import generics
from .models import RentForm
from .serializers import RentFormSerializer

class RentFormView(generics.ListCreateAPIView):
    queryset = RentForm.objects.all()
    serializer_class = RentFormSerializer