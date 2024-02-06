# Generated by Django 5.0.2 on 2024-02-06 20:53

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manufacturing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('shipping', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('taxes', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('material', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manufacturing.material')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acquisition.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acquisition.order')),
                ('supplier', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acquisition.supplier')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='acquisition.Record', to='acquisition.item'),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('taxes', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('link', models.URLField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acquisition.item')),
                ('supplier', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acquisition.supplier')),
            ],
        ),
    ]
