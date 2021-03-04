from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Creates the Contact Us form.
    """
    class Meta:
        # which model and which fields
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'subject',
            'your_message',
            )
