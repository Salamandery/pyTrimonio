from django.shortcuts import render
from .models import Celular
# Create your views here.

def index(request):
    celulares = Celular.objects.all()
    context = {
        'celulares': celulares
    }

    return render(request, 'celulares/index.html', context)