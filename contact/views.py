from django.shortcuts import render
from .forms import ContactForm


# Create your views here.

def contact(request):
    """
    Creates contact page, and sends contact form message
    """

    contact_form = ContactForm(request.POST)

    context = {
        'contact_form': contact_form,
    }
    template = 'contact/contact.html'
    return render(request, template, context)
