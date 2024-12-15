from django.db import models
from django.utils.timezone import now

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(default=now)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Image field

    def __str__(self):
        return self.title
