from django.db import models

# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=70)
    slug = models.SlugField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.name

