from django.shortcuts import render, redirect
from aumigos.forms import AumigosForm
from aumigos.models import Aumigos

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
    if request.method == 'POST':
        form = AumigosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request, 'index.html')
        

    context = {
        'nome_pagina': 'Cadastrar Pet',
        'form': form,
        'messages': form.errors,
    }
    return render(request, 'cadastrar_pet.html', context)