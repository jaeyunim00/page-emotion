from django.db import models

# Create your models here.
class YouTubeComment(models.Model):
  video_url = models.URLField()
  comment_text = models.TextField()
  sentiment_score = models.FloatField()

  def __str__(self):
    return f"{self.video_url} - {self.comment_text[:50]}..."