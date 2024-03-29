# Generated by Django 5.0.2 on 2024-02-08 13:43

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Iteration",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("description", models.TextField(blank=True, default="")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("created", "Created"), ("built", "Built")],
                        max_length=7,
                    ),
                ),
            ],
            options={
                "ordering": ("created_at",),
            },
        ),
        migrations.CreateModel(
            name="Prototype",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, default="")),
            ],
        ),
        migrations.CreateModel(
            name="Composition",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("quantity", models.DecimalField(decimal_places=3, max_digits=10)),
                (
                    "material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prototyping_composition_set",
                        to="inventory.material",
                    ),
                ),
                (
                    "iteration",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="prototyping.iteration",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="iteration",
            name="prototype",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="prototyping.prototype"
            ),
        ),
    ]
