# Generated by Django 5.0.6 on 2024-05-12 03:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aumigos', '0008_rename_photo_photo_foto_alter_photo_aumigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aumigos',
            name='foto',
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='foto')),
                ('aumigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aumigos.aumigos')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
                'ordering': ('pk',),
            },
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]