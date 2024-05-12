# Generated by Django 5.0.6 on 2024-05-12 02:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aumigos', '0006_aumigosfotos_remove_aumigos_foto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='foto')),
                ('aumigo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aumigos', to='aumigos.aumigos', verbose_name='foto')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
                'ordering': ('pk',),
            },
        ),
        migrations.DeleteModel(
            name='AumigosFotos',
        ),
        migrations.AlterField(
            model_name='aumigos',
            name='foto',
            field=models.ManyToManyField(blank=True, related_name='fotos', to='aumigos.photo', verbose_name='Foto do aumigo'),
        ),
    ]