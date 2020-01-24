from django.db import models
from django.urls import reverse

# Create your models here.
class Location(models.Model):
    street = models.CharField(max_length=100, default="High Street")
    number = models.DecimalField(max_digits=5, decimal_places=0, default="120")
    postcode = models.CharField(max_length=12, default="HP1 3AR")
    town = models.CharField(max_length=100, default="Hemel Hempstead")
    email = models.EmailField(default="info@callingmrschristmas.com")

    def get_absolute_url(self):
        return reverse("contact:location", kwargs={"pk": self.id})

    def __str__(self):
        return self.town

class ContactMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(blank=False, null=False, max_length=2000)
    date_sent = models.DateField(auto_now=True)
    reply = models.TextField(max_length=2000, blank=True, null=True)
    date_replied = models.DateField(blank=True, null=True)
