
from django import forms 
from .models import Pais

class PaisForm (forms.Form):
    class Meta:
        model = Pais

        nombrePais=forms.CharField(label='Nombre de país',max_length=100)
