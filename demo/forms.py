from django import forms
from .models import Post


class Upload(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'image_caption', 'image', ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image_caption': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'mt-3 border-0'}),
        }
