# CursosDjango/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from contenido import views as contenido_views

urlpatterns = [
    # Admin estándar (sin personalización)
    path('admin/', admin.site.urls),

    # Sitio principal
    path('', contenido_views.mprincipal, name="Principal"),
    path('cursos/', include('cursos.urls', namespace='cursos')),
    path('contacto/', contenido_views.contacto, name="Contacto"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
