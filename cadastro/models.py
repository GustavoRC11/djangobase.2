from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Contato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    assunto = models.CharField(max_length=250)
    mensagem = models.CharField(max_length=250)

    def __str__(self):
        return self.nome
