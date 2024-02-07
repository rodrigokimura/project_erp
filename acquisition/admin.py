from django.contrib import admin

from .models import Order, Record, Source, Supplier


class RecordInline(admin.TabularInline):
    model = Record


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ["supplier", "material", "quantity", "subtotal", "link"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "shipping", "taxes"]
    inlines = [RecordInline]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
