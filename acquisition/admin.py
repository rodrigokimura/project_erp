from django.contrib import admin

from .models import Item, Order, Record, Source, Supplier


class SourceInline(admin.TabularInline):
    model = Source


class RecordInline(admin.TabularInline):
    model = Record


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    inlines = [SourceInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "shipping", "taxes"]
    inlines = [RecordInline]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
