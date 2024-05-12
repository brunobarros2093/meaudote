from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios.views import index, cadastrar_pet, mais_informacoes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cadastrar_pet/', cadastrar_pet, name='cadastrar_pet'),
    path('mais_informacoes/<int:id>', mais_informacoes, name='mais_informacoes'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')
]
