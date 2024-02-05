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


class Bill(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="bill"
    )
    materials = models.ManyToManyField(Material, through="Line")


class Line(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)


class Source(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
