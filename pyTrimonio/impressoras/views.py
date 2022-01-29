from django.shortcuts import render
from .models import Impressora

# Create your views here.
def index(request):
    impressoras = Impressora.objects.all()
    context = {
        'impressoras': impressoras
    }

    return render(request, 'impressoras/index.html', context)