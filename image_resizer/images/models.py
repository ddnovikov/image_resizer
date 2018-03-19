import os

import PIL

from django.db import models
from django.urls import reverse

from .exceptions import AlreadyExistsError
from .utils import generate_hash


def image_upload_location(instance, filename):
    base, ext = os.path.splitext(filename)
    return f'images/{instance.image_hash}{ext}'


class Image(models.Model):
    image = models.ImageField(upload_to=image_upload_location,
                              height_field='height',
                              width_field='width',
                              verbose_name='Изображение')
    height = models.IntegerField(default=0, blank=True)
    width = models.IntegerField(default=0 ,blank=True)

    image_hash = models.CharField(max_length=32, blank=True, null=False, unique=True)

    class Meta:
        db_table = "images"
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __repr__(self):
        return f'Image(title={self.image_hash})'

    def __str__(self):
        return self.image_hash

    def save(self, *args, **kwargs):
        if self.pk is None:
            hash_ = generate_hash(self)
            self.image_hash = hash_
            if Image.objects.filter(image_hash=hash_):
                raise AlreadyExistsError('Image already exists.')
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:resize', kwargs={'image_hash': self.image_hash})

    def get_resized(self, width=None, height=None):
        if width is None:
            width = self.width
        if height is None:
            height = self.height

        pil_obj = PIL.Image.open(self.image.path)
        pil_obj = pil_obj.resize((int(width), int(height)), PIL.Image.ANTIALIAS)
        return pil_obj
