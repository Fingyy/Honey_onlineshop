from django.db import models


class Honey(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='honey_images/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class DeliveryAndPay(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
