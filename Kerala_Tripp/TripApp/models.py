from django.db import models


# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=250)
    img = models.FileField(upload_to='img')
    desc = models.TextField()

    def __str__(self):
        return self.name