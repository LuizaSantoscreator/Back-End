from django.urls import path
from .views import *

urlpatterns = [
    path('autores', AutorView.as_view())
]
