from django.shortcuts import render
from .models import Cr

# Create your views here.
def index(request):
    crs = Cr.objects.all()
    context = {
        'crs': crs
    }

    return render(request, 'cr/index.html', context)