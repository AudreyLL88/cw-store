from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('add/', views.add_blogpost, name='add_blogpost'),
    path('<int:blogpost_id>/', views.blog_detail, name='blog_detail'),
]
