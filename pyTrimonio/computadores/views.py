from django.shortcuts import render
from .models import Computador

# Create your views here.
def index(request):
    computadores = Computador.objects.all()
    context = {
        'computadores': computadores
    }

    return render(request, 'computadores/index.html', context)