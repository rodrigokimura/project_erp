from uuid import uuid4

from django.db import models


class Prototype(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")

    def __str__(self):
        return str(self.name)


class Material(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
