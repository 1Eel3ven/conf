from django.forms import ModelForm, CharField, DateTimeInput

from django.utils import timezone
from datetime import timedelta

from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'categories', 'text']