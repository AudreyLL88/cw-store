from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    blog_title = models.CharField(
        max_length=254, null=True, blank=True)
    blog_content = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.blog_title