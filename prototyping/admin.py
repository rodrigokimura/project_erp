from django.contrib import admin

from .models import Composition, Iteration, Prototype


class CompositionInline(admin.TabularInline):
    model = Composition


class IterationInline(admin.TabularInline):
    model = Iteration
    extra = 0
    show_change_link = True


@admin.register(Prototype)
class PrototypeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        # "product",
    ]
    inlines = [IterationInline]


@admin.register(Iteration)
class IterationAdmin(admin.ModelAdmin):
    list_display = [
        "prototype",
        "status",
        "description",
        "created_at",
        "estimated_cost",
    ]
    inlines = [CompositionInline]
