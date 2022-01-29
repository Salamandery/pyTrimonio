from django.shortcuts import render
from .models import Empresa

# Create your views here.
def index(request):
    empresas = Empresa.objects.all()
    context = {
        'empresas': empresas
    }

    return render(request, 'empresas/index.html', context)