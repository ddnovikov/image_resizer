import os

from django.db import models

from .utils import generate_hash


def image_upload_location(instance, filename):
    base, ext = os.path.splitext(filename)
    return f'images/{instance.image_hash}{ext}'


class Image(models.Model):
    image = models.ImageField(upload_to=image_upload_location,
                              height_field='height_field',
                              width_field='width_field',
                              blank=True,
                              null=True,
                              verbose_name='Изображение')
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)

    image_hash = models.CharField(max_length=32, null=False, unique=True)

    class Meta:
        db_table = "images"
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __repr__(self):
        return f'Image(title={self.name})'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            hash_ = generate_hash(self)
            self.image_hash = hash_
        super(Image, self).save(*args, **kwargs)
