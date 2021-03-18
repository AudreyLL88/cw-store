from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    """
    Display all items in the shopping bag.

    Parameters:
    request.

    Returns:
    Render: request and bag template.

   """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Allows items to be added to shopping bag.

    Parameters:
    request: the POST request from the form.
    item_id: the ID of the item added to the bag

    Returns:
    Redirect: to product url (stays on the same page)

   """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST.keys():
        size = request.POST['product_size']
    bag = request.session.get('bag', {})
    total_quantity = quantity

    # check item availability against stock
    if item_id in list(bag.keys()):
        if size:
            for item_size in bag[item_id]['items_by_size']:
                total_quantity += bag[item_id]['items_by_size'][item_size]
        else:
            total_quantity += bag[item_id]
    if total_quantity > product.qty:
        messages.warning(
                        request,
                        f'Oops, only {product.qty} of '
                        f'{product.name} left in stock. '
                        f'Please revise your order. ')
        return redirect(redirect_url)

    # quantity and size relations
    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                        request,
                        f'Updated size {size.upper()}'
                        f'{product.name} quantity to'
                        f'{bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                        request,
                        f'Added size {size.upper()}'
                        f'{product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                        request,
                        f'Added size {size.upper()}'
                        f'{product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                        request,
                        f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Allows the user the adjust the number and size of items in the bag

    Parameters:
    request: the POST request from the form.
    item_id: the ID of the item added to the bag

    Returns:
    Redirect: to product url (stays on the same page)

   """

    quantity = int(request.POST.get('quantity'))
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    # Adjust size if any.
    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Allows user to remove a product from the bag

    Parameters:
    request: the POST request from the form.
    item_id: the ID of the item added to the bag

    Returns:
    HttpsResponse: 500 or 200 response in the console

   """
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                    request,
                    f'Removed size {size.upper()}'
                    f'{product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
