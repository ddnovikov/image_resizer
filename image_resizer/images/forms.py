from django import forms

from .models import Image


class ImageForm(forms.ModelForm):
    image = forms.ImageField(required=False,
                             label='Изображение')
    url = forms.URLField(required=False,
                         label='Ссылка на изображение')
    class Meta:
        model = Image
        fields = [
            'image'
        ]
