from uuid import uuid4

from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField()
    materials = models.ManyToManyField("Material", through="Composition")

    def __str__(self):
        return str(self.name)


class Material(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Composition(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


class Order(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


class Process(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)


class Task(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    duration = models.DurationField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.name)
