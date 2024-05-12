from django import forms 
from .models import Aumigos, Photo

class AumigosForm(forms.ModelForm):
    class Meta:
        model = Aumigos
        fields = ['cidade', 'localidade', 'porte', 'nome', 'foto']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'porte': forms.Select(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'adotado': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'contato': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }
class PhotoForm(forms.ModelForm):
    photo = forms.ImageField(label='Foto')
    class Meta:
        model = Photo
        fields = ['photo']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }