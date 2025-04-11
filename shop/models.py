from django.core.validators import MinValueValidator
from django.db import models


class Honey(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='honey_images/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Packaging(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class HoneyProductOnStock(models.Model):
    honey_name = models.ForeignKey(Honey, on_delete=models.CASCADE)
    honey_packaging = models.ForeignKey(Packaging, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    """UniqueConstraint zajistí, že do Modelu nepřidám stejnou položku 2x (je to bezpečnost na úrovni databáze)"""

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['honey_name'], name='unique_product')
        ]

    def __str__(self):
        return f'{self.honey_name} - {self.honey_packaging.name}'


class DeliveryAndPay(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
