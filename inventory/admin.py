from django.contrib import admin
from .models import Item, Material, Tool
from acquisition.models import Source


class SourceInline(admin.TabularInline):
    model = Source


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "estimated_price"]
    inlines = [SourceInline]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["name", "estimated_price", "unit"]


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ["name", "estimated_price", "lifetime_in_years"]
