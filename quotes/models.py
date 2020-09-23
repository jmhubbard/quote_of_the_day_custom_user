from django.db import models
from shows.models import Show, Episode

# Create your models here.
class Quote(models.Model):
    quote_text = models.TextField(unique=True)
    speaker_name = models.CharField(max_length=255)
    show_name = models.ForeignKey(Show, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.quote_text}"
        # return f"{self.quote_text} by {self.speaker_name} - {self.show_name} - {self.season_number} - {self.episode_title}"


    def get_email_representation(self):
        return str(self)