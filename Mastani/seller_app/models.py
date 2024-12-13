from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
