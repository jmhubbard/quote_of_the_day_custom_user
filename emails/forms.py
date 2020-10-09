from django import forms
from django.core.mail import send_mail
import os

class ContactForm(forms.Form):
    subjectchoices = (
        ('Unable to sign up','Unable to sign up'),
        ('Unable to delete account', 'Unable to delete account'),
        ("Can't update subscriptions", "Can't update subscriptions"),
        ('Problems with a specific quote','Problems with a specific quote'),
        ('Suggestions for TV shows to add','Suggestions for TV shows to add'),
        ('Other','Other')
    )

    subject = forms.ChoiceField(choices= subjectchoices)
    message = forms.CharField(widget=forms.Textarea)
    user_email_address = forms.EmailField()
    
    def send_message(self):
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        useremail = self.cleaned_data['user_email_address']

        recipient_list = [os.getenv("EMAIL_HOST_USER")]
        
        mailmessage = f'Sender: {useremail}\nMessage: {message}'

        send_mail(
            f'Quote Of The Day Comment Form: {subject}',
            mailmessage,
            os.getenv("EMAIL_HOST_USER"),
            recipient_list,
            fail_silently=False
        )