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

    if request.method == 'POST':
        if image_form.is_valid():
            try:
                if image_form.cleaned_data['image']:
                    image = image_form.cleaned_data['image']
                    image_instance = Image(image=image)
                    image_instance.save()

                elif image_form.cleaned_data['url']:
                    url = image_form.cleaned_data['url']
                    Image.save_from_url(url)

            except AlreadyExistsError:
                messages.error(request, 'В системе уже есть точно такое же изображение. '
                                        'Загрузка одинаковых изображений запрещена.')
                return redirect('images:upload')

            messages.success(request, 'Изображение успешно загружено.')
            return redirect('images:home')

    context = {
        'form': image_form,
        'title': 'Загрузить изображение',
        'submit_value': 'Загрузить',
    }

    return render(request, 'upload.html', context)


def images_get_resized(request, image_hash):
    width = int(request.GET.get('width')) if request.GET.get('width') else None
    height = int(request.GET.get('height')) if request.GET.get('height') else None
    size = int(request.GET.get('size')) if request.GET.get('size') else None

    image = Image.objects.filter(image_hash=image_hash).first()
    buffer = image.get_resized(width, height, size)

    response = HttpResponse(content_type='image/jpg')
    response.write(buffer)

    return response


def images_resize(request, image_hash):
    width = request.GET.get('width') or ''
    height = request.GET.get('height') or ''
    size = request.GET.get('size') or ''

    context = {'width': width,
               'height': height,
               'size': size,
               'image_hash': image_hash,
               'submit_value': 'Изменить размер',
    }

    return render(request, 'resize.html', context=context)
