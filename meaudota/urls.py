from django.contrib import admin
from django.urls import path
from usuarios.views import index, cadastrar_pet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cadastrar_pet/', cadastrar_pet, name='cadastrar_pet')
]
