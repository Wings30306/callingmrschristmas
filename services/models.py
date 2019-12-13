from django.db import models
from django.core.files.storage import default_storage as storage

# Create your models here.


class ServiceCategory(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    description = models.TextField()
    name_for_image = models.CharField(max_length=100)
    img_alt = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    brief_description = models.TextField()
    detailed_description = models.TextField()
    img_name = models.CharField(max_length=100)
    img_alt = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=9, default=4.99)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
