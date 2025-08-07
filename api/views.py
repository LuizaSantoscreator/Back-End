from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Autor
from .serializers import AutorSerializer

class AutorView(ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer