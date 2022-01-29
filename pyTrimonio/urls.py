"""pyTrimonio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pyTrimonio.core.urls')),
    path('monitores/', include('pyTrimonio.monitores.urls')),
    path('computadores/', include('pyTrimonio.computadores.urls')),
    path('nobreaks/', include('pyTrimonio.nobreaks.urls'))
    path('impressoras/', include('pyTrimonio.impressoras.urls'))
    #path('celulares/', include('pyTrimonio.celulares.urls'))
    #path('toners/', include('pyTrimonio.toners.urls'))
    #path('empresas/', include('pyTrimonio.empresas.urls'))
    #path('estoques/', include('pyTrimonio.estoques.urls'))
    #path('produtos/', include('pyTrimonio.produtos.urls'))
    path('admin/', admin.site.urls),
]
