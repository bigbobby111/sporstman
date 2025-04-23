from django.db import models

# Create your models here.


class NewsItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    time = models.DateTimeField()
    image = models.ImageField(upload_to='news_images/')
    is_slider = models.BooleanField(default=False)

    def __str__(self):
        return self.title
