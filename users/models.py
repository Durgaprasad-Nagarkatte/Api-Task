from django.contrib.auth.models import AbstractUser
from django.db import models
import pytz

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    user_id = models.CharField(max_length=9, unique=True)
    
