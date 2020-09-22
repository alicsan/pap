from django.shortcuts import render
from pais.models import Pais
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from pais.forms import PaisForm

# Create your views here.

def home (request) :
    return render(request,'home.html')
    
    
def crear_vista(request) :
    if request.method == 'POST':
        form = PaisForm(request.POST or None)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = PaisForm()

    return render(request, 'cPais.html', {'form': form})
