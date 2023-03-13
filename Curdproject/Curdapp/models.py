from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='movieimages-')
    description = models.TextField()
    released_at = models.DataField(auto_now_add=True)


    def __str__(self):
        return self.name

class Slides(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images")

    def _str_(self):
        return self.name