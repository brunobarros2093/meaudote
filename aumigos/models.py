from django.db import models

# Create your models here.


class Aumigos(models.Model):
    PORTES = [('pequeno', 'Pequeno'), ('medio', 'Médio'), ('grande', 'Grande')]
    cidade = models.CharField(
        max_length=255,
        verbose_name='Cidade do aumigo',
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
    contato = models.ManyToOneRel(
        'usuarios.Usuarios',
        to='usuarios.Usuarios',
        field_name='usuario',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome
