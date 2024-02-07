from django.contrib import admin

from acquisition.models import Source

from .models import Item, Material, Tool


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
