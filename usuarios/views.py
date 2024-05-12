from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('index.html')
        

    context = {
        'nome_pagina': 'Cadastrar Pet',
        'form': form,
    }
    return render(request, 'cadastrar_pet.html', context)

def mais_informacoes(request, id):
    pet = get_object_or_404(Aumigos, id=id)
    context = {
        'nome_pagina': 'Mais Informações',
        'form': pet,
    }
    return render(request, 'mais_informacoes.html', context)