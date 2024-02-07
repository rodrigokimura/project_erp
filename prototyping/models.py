from uuid import uuid4

from django.db import models


class Prototype(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return str(self.name)


class Iteration(models.Model):
    STATUS_CHOICES = (
        ("created", "Created"),
        ("built", "Built"),
    )
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=7)
    prototype = models.ForeignKey(Prototype, on_delete=models.CASCADE)

    class Meta:  # type: ignore
        ordering = ("created_at",)

    def __str__(self):
        count = self.__class__.objects.filter(
            prototype=self.prototype, created_at__lte=self.created_at
        ).count()
        return f"{self.prototype.name} #{count}"

    @property
    def estimated_cost(self):
        compositions = Composition.objects.filter(iteration=self)
        cost = 0
        for c in compositions:
            cost += getattr(c.material, "estimated_price", 0) * c.quantity
        return cost


class Composition(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    iteration = models.ForeignKey(Iteration, on_delete=models.CASCADE)
    material = models.ForeignKey(
        "inventory.Material",
        on_delete=models.CASCADE,
        related_name="prototyping_composition_set",
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
