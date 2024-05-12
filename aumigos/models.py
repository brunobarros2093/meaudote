from django.db import models
from usuarios.models import Usuarios

class Aumigos(models.Model):
    PORTES = [('PEQUENO', 'Pequeno'), ('MEDIO', 'Médio'), ('GRANDE', 'Grande')]
    cidade = models.CharField(
        max_length=255,
        verbose_name='Cidade do aumigo',
        null=False,
    )
    localidade = models.CharField(
        max_length=255,
        verbose_name='Localidade do aumigo [mais especifico que cidade]',
        null=False,
    )
    porte = models.CharField(
        max_length=255,
        verbose_name='Porte do aumigo',
        choices=PORTES
    )
    nome = models.CharField(
        max_length=255,
        verbose_name='Nome do aumigo(a)',
        null=True,
        blank=True
    )
    foto = models.ManyToManyField('aumigos.Photo', verbose_name='Foto do aumigo', related_name='fotos', blank=True)
    adotado = models.BooleanField(
        default=False,
        verbose_name='Aumigo foi adotado?',
    )
    contato = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
    
    def get_adotado(self):
        if self.adotado:
            return 'Sim'
        else:
            return 'Não'

class Photo(models.Model):
    photo = models.ImageField('foto', upload_to='')
    aumigo = models.ForeignKey(Aumigos,verbose_name='foto', related_name='aumigos', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('pk', )
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
    def __str__(self):
        return str(self.aumigo)