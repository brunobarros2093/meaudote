from django.shortcuts import render, redirect
from aumigos.forms import AumigosForm
from aumigos.models import Aumigos
from usuarios.models import Usuarios

# Create your views here.
def index(request):
    pets = Aumigos.objects.all().filter(id=request.user.id)
    context = {
        'nome_pagina': 'MeauDota Home',
        'pets': pets,
    }
    return render(request, 'index.html', context)


def cadastrar_pet(request):
    form = AumigosForm()
    #contato = Usuarios.objects.get(id=request.user.id).contato
    if request.method == 'POST':
        form = AumigosForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.contato = Usuarios.objects.get(id=request.user.id).contato
            return redirect(request, 'index.html')
        

    context = {
        'nome_pagina': 'Cadastrar Pet',
        'form': form,
    }
    return render(request, 'cadastrar_pet.html', context)

def mais_informacoes(request):
    pet = Aumigos.objects.get(id=id)
    context = {
        'nome_pagina': 'Mais Informações',
        'pet': pet,
    }
    return render(request, 'mais_informacoes.html', context)