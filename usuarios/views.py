from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from aumigos.forms import AumigosForm
from aumigos.models import Aumigos

# Create your views here.
def index(request):
    pets = Aumigos.objects.all()
    paginated_by = 5
    context = {
        'nome_pagina': 'MeauDota Home',
        'pets': pets,
    }
    return render(request, 'index.html', context)

@login_required
def cadastrar_pet(request):
    form = AumigosForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            #for photo in photos:
            return redirect('mais_informacoes.html', id=form.instance.id)
        
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

