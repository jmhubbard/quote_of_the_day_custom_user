from django.db import models
import users.models
import shows.models

# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    show = models.ForeignKey('shows.Show', on_delete=models.CASCADE)
    is_subscribed = models.BooleanField(default=True)
