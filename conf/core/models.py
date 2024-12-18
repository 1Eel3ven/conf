from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    categories = models.ManyToManyField(Category)

    title = models.CharField(max_length=255)
    text = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
