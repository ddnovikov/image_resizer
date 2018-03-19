from django.urls import path, re_path

from . import views

app_name = 'images'


urlpatterns = [
    path('', views.images_home, name='home'),
    path('upload/', views.images_upload, name='upload'),
    re_path('^(?P<image_hash>[a-z\d]{32})/get-resized-img/$', views.images_get_resized, name='get-resized'),
    re_path('^(?P<image_hash>[a-z\d]{32})/$', views.images_resize, name='resize'),
]
