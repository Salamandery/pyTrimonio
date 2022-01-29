from django.shortcuts import render
from .models import Nobreak

# Create your views here.
def index(request):
    nobreaks = Nobreak.objects.all()
    context = {
        'nobreaks': nobreaks
    }

    return render(request, 'nobreaks/index.html', context)