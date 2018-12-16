from django.db import models

# Create your models here.
# class Profile(models.Model):
#     prof_pic = models.ImageField()
#     Bio = models.TextField()


class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=40)
    caption = models.TextField()
    likes = models.IntegerField()
    comments = models.TextField()

