from django.db import models
import users.models

class EmailTracker(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    last_quote_email = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.user}'s last daily email was sent on {self.last_quote_email}"
