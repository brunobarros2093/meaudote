from django.db import models
from usuarios.models import Usuarios

# Create your models here.


class Aumigos(models.Model):
    PORTES = [('pequeno', 'Pequeno'), ('medio', 'Médio'), ('grande', 'Grande')]
    cidade = models.CharField(
        max_length=255,
        verbose_name='Cidade do aumigo',
        null=False,
    )
    localidade = models.CharField(
        max_length=255,
        verbose_name='Localidade do aumigo [mais especifico que cidade]',
        null=False,
        default='Não informado',
    )
    porte = models.CharField(
        max_length=255,
        verbose_name='Porte do aumigo',
        choices=PORTES
    )
    nome = models.CharField(
        max_length=255,
        verbose_name='Nome do aumigo',
    )
    foto = models.ImageField(
        upload_to='./fotos/',
        verbose_name='Foto do aumigo',
    )
    adotado = models.BooleanField(
        default=False,
        verbose_name='Aumigo foi adotado?',
    )
    contato = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
