from django import forms 
from .models import Aumigos

class AumigosForm(forms.ModelForm):
    class Meta:
        model = Aumigos
        fields = '__all__'
