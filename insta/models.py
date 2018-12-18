from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    prof_pic = models.ImageField()
    Bio = models.TextField()


class Image(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'photos/')
    name = models.CharField(max_length=40)
    caption = models.TextField()
    likes = models.IntegerField()
    comments = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

