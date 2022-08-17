from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=300)
    photo = models.ImageField(upload_to = 'content', null = True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home-page')