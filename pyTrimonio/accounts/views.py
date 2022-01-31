from pyTrimonio.logging import Logger
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import RegisterForm
# Create your views here.
logger = Logger()

def register(request):
    template_name = 'accounts/register.html'
    
    context = {
        'form': RegisterForm()
    }

    logger.info(context)

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            logger.info('Cadastro realizado com sucesso!')
            form.save()
            return redirect(settings.LOGIN_URL)

    return render(request, template_name, context)