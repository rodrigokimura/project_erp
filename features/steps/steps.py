from behave import given, then, when

from inventory.models import Item, Material, Tool

# ruff: noqa: F811


@given("there are no items")
def step_impl(context):
    assert Item.objects.exists() is False


@when("a material is created")
def step_impl(context):
    material = Material.objects.create(name="vibranium", unit="un")

    assert material.id


@when("a tool is created")
def step_impl(context):
    tool = Tool.objects.create(name="3d printer", lifetime_in_years=10)

    assert tool.id


@then("there will be an item")
def step_impl(context):
    assert Item.objects.count() == 1
