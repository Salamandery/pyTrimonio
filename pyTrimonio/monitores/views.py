from django.shortcuts import render
from .models import Monitor

# Create your views here.
def index(request):
    monitores = Monitor.objects.all()
    context = {
        'monitores': monitores
    }

    return render(request, 'monitores/index.html', context)