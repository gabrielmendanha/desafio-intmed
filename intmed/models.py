from django.db import models


class Item(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.IntegerField()


class Mercado(models.Model):
    nome = models.CharField(max_length=100)
    estoque = models.ManyToManyField(Item, blank=True)


class Entrega(models.Model):
    remetente = models.ForeignKey(Mercado)
    destino = models.CharField(max_length=100)
    produtos = models.ManyToManyField(Item)
    data = models.DateTimeField()
    total = models.IntegerField()
