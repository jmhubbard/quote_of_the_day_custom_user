from django.db import models
import users.models
from datetime import date, timedelta, datetime

def create_email_tracker_for_user_on_creation(user):
    current_time = datetime.now()
    user_email_tracker = EmailTracker(user = user, last_quote_email = current_time)
    user_email_tracker.save()
    
    


class EmailTracker(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    last_quote_email = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.user}'s last daily email was sent on {self.last_quote_email}"
