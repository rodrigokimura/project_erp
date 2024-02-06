from django.contrib import admin

from .models import Expense, Income


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ["name"]
