from django.http import HttpResponse
from django.shortcuts import render

from .models import Image


def images_home(request):
    image_list = Image.objects.all()
    return render(request, 'home.html', context={'image_list': image_list})


def images_upload(request):
    pass


def images_get_resized(request, image_hash):
    width = request.GET.get('width') or None
    height = request.GET.get('height') or None

    image = Image.objects.filter(image_hash=image_hash).first()
    pil_obj = image.get_resized(width, height)

    response = HttpResponse(content_type='image/jpg')
    pil_obj.save(response, 'JPEG')

    return response


def images_resize(request, image_hash):
    width = request.GET.get('width') or ''
    height = request.GET.get('height') or ''

    context = {'width': width,
               'height': height,
               'image_hash': image_hash
    }

    return render(request, 'resize.html', context=context)
