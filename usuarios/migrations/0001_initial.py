# Generated by Django 5.0.6 on 2024-05-11 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aumigos', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=194, unique=True, verbose_name='E-mail do usuário')),
                ('is_active', models.BooleanField(default=True, verbose_name='Usuario esta ativo')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Usuário é da equipe de desenvolvimento')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Usuário é um superusuario')),
                ('aumigos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aumigos.aumigos')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuarios',
            },
        ),
    ]
