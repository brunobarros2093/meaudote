# Generated by Django 5.0.6 on 2024-05-11 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aumigos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do aumigo')),
                ('cidade', models.CharField(max_length=255, verbose_name='Cidade do aumigo')),
                ('porte', models.CharField(max_length=255, verbose_name='Porte do aumigo')),
                ('idade', models.IntegerField(verbose_name='Idade do aumigo')),
                ('descricao', models.TextField(verbose_name='Descrição do aumigo')),
                ('foto', models.ImageField(upload_to='aumigos/', verbose_name='Foto do aumigo')),
                ('adotado', models.BooleanField(default=False, verbose_name='Aumigo foi adotado?')),
            ],
        ),
    ]
