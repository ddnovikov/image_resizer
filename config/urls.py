from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from image_resizer.images import urls as images_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(images_urls, namespace='images')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
