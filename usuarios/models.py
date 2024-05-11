from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin
)

class UsuarioManager(BaseUserManager):

    def create_user(self, email, password=None):
        usuario = self.model(
            email=self.normalize_email(email)
        )
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)
        usuario.save()

        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(self.normalize_email(email), password)

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()

        return usuario


class Usuarios(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        verbose_name='E-mail do usuário',
        max_length=194,)
    is_active = models.BooleanField(
        verbose_name='Usuario esta ativo',
        default=True,
    )
    is_staff = models.BooleanField(
        verbose_name="Usuário é da equipe de desenvolvimento",
        default=False,
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name="Usuário é um superusuario"
    )
    # 1-N com Pets
    aumigos = models.ForeignKey('aumigos.Aumigos', on_delete=models.CASCADE, null=True, blank=True)
    USERNAME_FIELD = "email"
    # atribui a criação de usuário para o novo Manager
    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        db_table = "usuarios"

    def __str__(self):
        return self.email
