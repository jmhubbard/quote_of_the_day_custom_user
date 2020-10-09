from django.shortcuts import render
from emails.forms import ContactForm
from django.shortcuts import redirect

from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin

class ContactView(SuccessMessageMixin, FormView):
    template_name = 'emails/contactform.html'
    form_class = ContactForm
    success_url = reverse_lazy('contactform')
    success_message = 'Your message was sent'

    def form_valid(self, form):
        form.send_message()
        return super().form_valid(form)
