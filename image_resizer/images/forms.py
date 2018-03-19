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

    def clean(self):
        cleaned_data = super(ImageForm, self).clean()

        if not (cleaned_data.get('url') or cleaned_data.get('image')):
            self.add_error(None, 'Необходимо заполнить одно поле.')

        if cleaned_data.get('url') and cleaned_data.get('image'):
            self.add_error(None, 'Необходимо заполнить только одно поле.')
