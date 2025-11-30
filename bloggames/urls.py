from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # CORE → Aquí está tu API de productos
    path('', include('core.urls')),

    path('comunidad/', include('comunidad.urls')),
    path('galeria/', include('galeria.urls')),
    path('noticias/', include('noticias.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
    path('api/', include('api_app.urls')),

    # ⚠ DÉJALE UN PREFIJO A ESTA APP
    path('consumer/', include('consumer.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'core.views.custom_404'
