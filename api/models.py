from django.db import models

class Autor(models.Model): #models minusculo são as caracteristicas da tabela
    nome = models.CharField(max_length=255)#charField são campos de caracter
    sobrenome = models.CharField(max_length=255)# max_length defini quanto
    data_nascimento = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=30, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True) #textField não tem tamanho definido de texto

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    
