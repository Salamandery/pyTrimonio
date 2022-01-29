from django.shortcuts import render
from .models import Estoque

# Create your views here.
def index(request):
    estoques = Estoque.objects.all()
    context = {
        'estoques': estoques
    }

    return render(request, 'estoques/index.html', context)