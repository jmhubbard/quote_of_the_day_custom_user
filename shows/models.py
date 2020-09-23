from django.db import models
import users.models
from subscriptions.models import Subscription

# Create your models here.
class Show(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField('users.User', through=Subscription)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Episode(models.Model):
    name = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    season = models.PositiveIntegerField(null=True, blank=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
