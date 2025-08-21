from django.urls import path
from .views import *

urlpatterns = [
    path('autores', AutorView.as_view()),
    path('authors', list_autor),
    path('editoras', EditoraView.as_view()),
    path('livros', LivroView.as_view())
]
