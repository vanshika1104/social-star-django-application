from django import forms
from .models import Image, Comment
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model= Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }
        '''
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.split('.')[0].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given url is incorrect')
        return url
        '''

    def save(self, force_insert = False, force_update=False, commit=True):
        image = super(ImageCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title), image_url.rsplit('.',1)[0].lower())
        #download image from given urls
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save()
        return image

class EmailForm(forms.Form):
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')
        widgets = {
            'body': forms.Textarea,
            # 'name':forms.HiddenInput,
        }
