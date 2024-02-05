from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["id", "name"]
