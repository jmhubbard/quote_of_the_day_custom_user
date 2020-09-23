from django.db import models
from shows.models import Show, Episode, Character

# Create your models here.
class Quote(models.Model):
    text = models.TextField(unique=True)
    speaker_name = models.CharField(max_length=255)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, null=True)
    speaker = models.ForeignKey(Character, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.text}"
        # return f"{self.quote_text} by {self.speaker_name} - {self.show_name} - {self.season_number} - {self.episode_title}"


    def get_email_representation(self):
        return str(self)