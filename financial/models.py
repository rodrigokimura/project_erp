from uuid import uuid4

from django.db import models


class Base(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.name)

    class Meta:  # type: ignore
        abstract = True


class Expense(Base):
    order = models.ForeignKey(
        "acquisition.Order", on_delete=models.PROTECT, null=True, default=None
    )


class Income(Base):
    order = models.ForeignKey(
        "manufacturing.Order", on_delete=models.PROTECT, null=True, default=None
    )
