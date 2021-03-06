from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Employee(models.Model):
    """ Model to save employee profile data """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    intro = models.TextField()
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("about:about_detail", kwargs={"user": self.user.username})


class CaseStudy(models.Model):
    """ Model to save case study to showcase to visitors """
    title = models.CharField(max_length=100)
    client_first_name = models.CharField(max_length=100)
    client_last_name_initial = models.CharField(
        max_length=1, blank=True, null=True)
    client_company = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return 'Case Study: ' + self.title
