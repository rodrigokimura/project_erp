from django.contrib import admin

from .models import Composition, Order, Process, Product, Task


class CompositionInline(admin.TabularInline):
    model = Composition


class TaskInline(admin.TabularInline):
    model = Task


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "estimated_material_cost"]
    inlines = [CompositionInline]


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ["product"]
    inlines = [TaskInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["product"]
