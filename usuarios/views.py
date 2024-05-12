from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from aumigos.forms import AumigosForm, AumigosPhotoForm
from aumigos.models import Aumigos, Photo

# Create your views here.
def index(request):
    pets = Aumigos.objects.all().filter()
    context = {
        'nome_pagina': 'MeauDota Home',
        'pets': pets,
    }
    return render(request, 'index.html', context)

@login_required
def cadastrar_pet(request):
    form = AumigosPhotoForm(request.POST or None)
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        if form.is_valid():
            aumigo = form.save()
            #for photo in photos:
            Photo.objects.create(photo=photo, aumigo=aumigo)
            return redirect('mais_informacoes.html', id=aumigo.id)
        
    context = {
        'nome_pagina': 'Cadastrar Pet',
        'form': form,
    }
    return render(request, 'cadastrar_pet.html', context)

def mais_informacoes(request, id):
    pet = get_object_or_404(Aumigos, id=id)
    form = AumigosPhotoForm(request.POST)
    if request.method == 'POST':
        form = AumigosPhotoForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    context = {
        'nome_pagina': 'Mais Informações',
        'form': form,
        'pet':pet 
    }
    return render(request, 'mais_informacoes.html', context)

