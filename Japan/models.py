from django.db import models
from django.conf import settings

class ContactInfo(models.Model):
    title = models.CharField(max_length=55)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title + '\n' + self.name + '\n' + self.description

class OrderInfo(models.Model):
    guests = models.IntegerField()
    acomodation = models.CharField(max_length=100)
    start_date = models.CharField(null=True, max_length=100)
    end_date = models.CharField(null=True, max_length=100)
    optional = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True)