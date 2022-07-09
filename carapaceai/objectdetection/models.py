from django.db import models
from django.utils import timezone

# Create your models here.
class History(models.Model):
    result_video = models.FileField(upload_to="videos/")
    tested_on = models.DateTimeField(default=timezone.now)
    passed = models.BooleanField(default=False)

class Video(models.Model):
    video = models.FileField(upload_to="video/")