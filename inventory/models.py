from uuid import uuid4

from django.db import models


class Item(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return str(self.name)


class Material(Item):
    UNIT_CHOICES = (
        ("un", "unit"),
        ("kg", "kilogram"),
        ("m", "meter"),
    )
    unit = models.CharField(
        max_length=3, choices=UNIT_CHOICES, default=UNIT_CHOICES[0][0]
    )

    def __str__(self):
        return str(self.name)


class Tool(Item):
    lifetime_in_years = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.name)


class Entry(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantity = models.FloatField()

    def __str__(self):
        return str(self.name)
