from django import forms 
from .models import Aumigos

class AumigosForm(forms.ModelForm):
    class Meta:
        model = Aumigos
        fields = ['cidade', 'localidade', 'porte', 'nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'porte': forms.Select(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }
class AumigosPhotoForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    class Meta:
        model = Aumigos
        fields = ['cidade', 'localidade', 'porte', 'nome', 'photo']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
