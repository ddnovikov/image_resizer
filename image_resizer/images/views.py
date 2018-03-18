from django.shortcuts import render

from .models import Image


def images_home(request):
    image_list = Image.objects.all()
    return render(request, 'home.html', context={'image_list': image_list})


def images_upload(request):
    pass


def images_resize(request, image_hash):
    pass
