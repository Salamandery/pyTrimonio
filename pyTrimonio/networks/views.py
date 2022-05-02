from django.shortcuts import render
from .models import Network
# Create your views here.

def index(request):
    networks = Network.objects.all()
    context = {
        'networks': networks
    }

    return render(request, 'networks/index.html', context)