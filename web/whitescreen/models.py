from django.db import models

class Matriz(models.Model):
    matriz_nome = models.CharField(max_length=200)
    qtd_linhas_m = models.IntegerField(default=0)
    qtd_colunas_n = models.IntegerField(default=0)

class Elemento(models.Model):
    matriz = models.ForeignKey(Matriz, on_delete=models.CASCADE)
    linha = models.IntegerField()
    coluna = models.IntegerField()
    valor = models.IntegerField()
