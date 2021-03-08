from django.contrib import admin
from .models import BlogPost

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    """ Creates the admin interface for Blog posts """
    list_display = (
        'blog_title',
        'author',
        'blog_content',
        'date'
    )


admin.site.register(BlogPost, BlogAdmin)
