from django.db import models
import users.models
from subscriptions.models import Subscription
from django.utils.translation import gettext as _

# Create your models here.
class Show(models.Model):
    TYPE_CHOICE_UNKNOWN = 0
    TYPE_CHOICE_MOVIE = 1
    TYPE_CHOICE_TV = 2
    TYPE_CHOICES = (
        (TYPE_CHOICE_UNKNOWN, _('Unknown')),
        (TYPE_CHOICE_MOVIE, _('Movie')),
        (TYPE_CHOICE_TV, _('TV')),
    )
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField('users.User', through=Subscription)
    category = models.IntegerField(
        choices = TYPE_CHOICES,
        default = TYPE_CHOICE_UNKNOWN,
    ) 
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Episode(models.Model):
    name = models.CharField(max_length=255)
    season = models.PositiveIntegerField(null=True, blank=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ("name", "season", "show"),
        )

    def __str__(self):
        return self.name

class Character(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ("first_name", "last_name", "show"),
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

