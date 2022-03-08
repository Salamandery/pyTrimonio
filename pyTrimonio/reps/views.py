from django.shortcuts import render
from .models import Rep

# Create your views here.
def index(request):
    reps = Rep.objects.all()
    context = {
        'reps': reps
    }

    return render(request, 'reps/index.html', context)