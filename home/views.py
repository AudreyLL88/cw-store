import random
from django.shortcuts import render
from products.models import Product


# Create your views here.


def index(request):
    """ A view to return the index page """

    suggestions = Product.objects.all()
    suggested_products = list(suggestions)

    # pick 3 random from suggested list
    suggested_products = random.sample(suggested_products, min(len(suggested_products), 4))

    context = {
        'suggested_products': suggested_products,
    }

    return render(request, 'home/index.html', context)
