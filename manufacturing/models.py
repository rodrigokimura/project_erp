from uuid import uuid4

from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.name)


class Material(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Compostition(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Source(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.SET_NULL, null=True, default=None
    )
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    link = models.URLField()
