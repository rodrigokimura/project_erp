from django.contrib import admin

from .models import Composition, Material, Product, Process, Task


class CompositionInline(admin.TabularInline):
    model = Composition


class TaskInline(admin.TabularInline):
    model = Task


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    inlines = [CompositionInline]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ["id", "product"]
    inlines = [TaskInline]
