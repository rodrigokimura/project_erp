from uuid import uuid4

from django.db import models
from manufacturing.models import Material


class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Item(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)
    material = models.OneToOneField(
        Material, on_delete=models.SET_NULL, null=True, default=None
    )

    def __str__(self):
        return str(self.name)


class Source(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.SET_NULL, null=True, default=None
    )
    material = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    link = models.URLField()


class Order(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    items = models.ManyToManyField(Item, through="Record")
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    # created_at
    # status


class Record(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.SET_NULL, null=True, default=None
    )
    quantity = models.PositiveSmallIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
