from datetime import timedelta
from uuid import uuid4

from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default="")
    materials = models.ManyToManyField("inventory.Material", through="Composition")
    prototype = models.OneToOneField(
        "prototyping.Prototype", on_delete=models.SET_NULL, null=True, default=None
    )

    @property
    def estimated_material_cost(self):
        compositions = Composition.objects.filter(product=self)
        cost = 0
        for c in compositions:
            cost += getattr(c.material, "estimated_price", 0) * c.quantity
        return cost

    def __str__(self):
        return str(self.name)


class Composition(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="manufacturing_composition_set"
    )
    material = models.ForeignKey(
        "inventory.Material",
        on_delete=models.CASCADE,
        related_name="manufacturing_composition_set",
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=3)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


class Process(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    class Meta:  # type: ignore
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
