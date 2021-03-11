from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.


class ReviewInline(admin.TabularInline):
    """ Allows view/edit of reviews from Product detail page """
    model = Review


class ProductAdmin(admin.ModelAdmin):
    """ Add products section in admin dashboard """

    list_display = (
        'sku',
        'name',
        'category',
        'size',
        'qty',
        'price',
        'image',
    )

    ordering = ('sku',)

    inlines = [
        ReviewInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    """ Add category section in admin dashboard """

    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """ Add product review section in admin dashboard """

    list_display = (
        'review_title',
        'reviewer',
        'product',
        'rating'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
