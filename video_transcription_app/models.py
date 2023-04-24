from django.db import models

# Create your models here.
class Video(models.Model):
    video_url  = models.CharField(max_length=250)
    transcript = models.TextField()