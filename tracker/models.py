from django.db import models
from users.models import CustomUser
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Tracker(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='activities')
    start_utc_time = models.DateTimeField(default=timezone.now)
    end_utc_time = models.DateTimeField(default=timezone.now)
    #start_time = models.DateTimeField(default=timezone.now)
    #end_time = models.DateTimeField(default=timezone.now)

