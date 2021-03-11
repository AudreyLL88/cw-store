from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from products.models import Review


@login_required
def profile(request):
    """
        Displays user profile and saves infos if changed.
        Includes order and review history.

        Parameters:
        request.

        Returns:
        Render: request, profile template and context

    """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    reviews = Review.objects.filter(reviewer=request.user)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'reviews': reviews,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):

    """
        Displays previous order details.

        Parameters:
        request.
        order_number: Unique number generated
        when order was successful.

        Returns:
        Render: request, checkout_success template and context.

    """

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
