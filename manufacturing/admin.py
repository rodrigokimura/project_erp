from django.contrib import admin

from .models import Composition, Material, Order, Process, Product, Task


class CompositionInline(admin.TabularInline):
    model = Composition


class TaskInline(admin.TabularInline):
    model = Task


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [CompositionInline]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["name", "estimated_cost"]


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ["product"]
    inlines = [TaskInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["product"]
