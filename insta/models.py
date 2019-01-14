from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    prof_pic = models.ImageField()
    Bio = models.TextField()

    @classmethod
    def search_user(cls,name):
        return User.objects.filter(username__icontains = name)


class Image(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'photos/')
    name = models.CharField(max_length=40)
    caption = models.TextField()
    likes = models.IntegerField(null=True)
    comments = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def save_image(self):
        self.save()

    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images


