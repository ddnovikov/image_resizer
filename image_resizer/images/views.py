from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .exceptions import AlreadyExistsError
from .forms import ImageForm
from .models import Image


def images_home(request):
    image_list = Image.objects.all()
    return render(request, 'home.html', context={'image_list': image_list})


def images_upload(request):
    image_form = ImageForm(request.POST or None, request.FILES or None)
    print(request.FILES)
    if request.method == 'POST':
        if image_form.is_valid() and request.FILES:
            image = image_form.cleaned_data['image']
            image_instance = Image(image=image)

            try:
                image_instance.save()
            except AlreadyExistsError:
                return HttpResponse('В системе уже есть точно такое же изображение. '
                                    'Загрузка одинаковых изображений запрещена.',
                                    status=405)

            messages.success(request, 'Изображение успешно загружено.')
            return redirect('images:home')

    context = {
        'form': image_form,
        'title': 'Загрузить изображение',
        'submit_value': 'Загрузить',
    }

    return render(request, 'upload.html', context)


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
