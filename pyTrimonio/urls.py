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
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'pyTrimonio - Admin'

urlpatterns = [
    path('', include('pyTrimonio.core.urls', namespace='core')),
    path('entrar/', include('pyTrimonio.accounts.urls', namespace='accounts')),
    path('monitores/', include('pyTrimonio.monitores.urls', namespace='monitores')),
    path('computadores/', include('pyTrimonio.computadores.urls', namespace='computadores')),
    path('cr/', include('pyTrimonio.cr.urls', namespace='cr')),
    path('nobreaks/', include('pyTrimonio.nobreaks.urls', namespace='nobreaks')),
    path('impressoras/', include('pyTrimonio.impressoras.urls', namespace='impressoras')),
    #path('celulares/', include('pyTrimonio.celulares.urls')),
    #path('toners/', include('pyTrimonio.toners.urls')),
    #path('empresas/', include('pyTrimonio.empresas.urls')),
    #path('estoques/', include('pyTrimonio.estoques.urls')),
    #path('produtos/', include('pyTrimonio.produtos.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
