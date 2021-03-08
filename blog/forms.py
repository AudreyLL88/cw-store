from django import forms
from products.widgets import CustomClearableFileInput
from .models import BlogPost


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
