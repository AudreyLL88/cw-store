from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm


# Create your views here.

def contact(request):
    """
    Creates contact page, and sends contact form message
    """

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            user_email = contact_form.cleaned_data['email']
            subject = (" Message Reception Confirmation: " +
                       contact_form.cleaned_data['subject'])
            body = render_to_string(
                'contact/emails/email_body.txt',
                {'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [user_email]
            )
        else:
            messages.error(request, 'Oops, looks like  there is an error. \
                Please verify the information submitted.')

    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }
    template = 'contact/contact.html'
    return render(request, template, context)
