from django.db import models
from django.utils import timezone


def user_directory_path(instance, filename):
    return 'posts/{0}/{1}'.format(instance.id, filename)


class Post(models.Model):

    title = models.CharField(max_length=250)
    image = models.ImageField(
        upload_to=user_directory_path)
    image_caption = models.CharField(
        max_length=100, default='Photo by demo')
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
