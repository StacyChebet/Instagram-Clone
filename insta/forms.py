from django import forms
from .models import Image

class postImage(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['poster','profile', 'comments', 'likes']
         