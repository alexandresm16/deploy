from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('taxasI/', include('taxasImobiliaria.urls')),
    path('taxasR/', include('taxasReajuste.urls')),
    path('proprietarios/', include('proprietario.urls')),
    path('clientes/', include('clientes.urls')),
    path('corretores/', include('corretor.urls')),
    path('imoveis/', include('imovel.urls')),
    path('visitas/', include('visita.urls')),
    path('transacoes/', include('transacao.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


