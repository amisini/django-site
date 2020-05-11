from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
    