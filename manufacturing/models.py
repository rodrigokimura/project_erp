from datetime import timedelta
from uuid import uuid4

from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default="")
    materials = models.ManyToManyField("Material", through="Composition")

    def __str__(self):
        return str(self.name)


class Material(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100, unique=True)
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return str(self.name)


class Composition(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="manufacturing_composition_set"
    )
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name="manufacturing_composition_set"
    )
    quantity = models.PositiveSmallIntegerField(default=0)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


class Process(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "process"
        verbose_name_plural = "processes"


class Task(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    duration = models.DurationField(default=timedelta)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.name)
