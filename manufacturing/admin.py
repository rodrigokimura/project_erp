from django.contrib import admin

from .models import Product, Material, Compostition, Source, Supplier


class CompositionInline(admin.TabularInline):
    model = Compostition


class SourceInline(admin.TabularInline):
    model = Source


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    inlines = [CompositionInline]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    inlines = [SourceInline]
