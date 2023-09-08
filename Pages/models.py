from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Game(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)