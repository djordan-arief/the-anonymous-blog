
from django.db import models

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to = 'profile')
    biography = models.TextField(max_length=200)


    def __str__(self):
        return "Creator's profile"

    