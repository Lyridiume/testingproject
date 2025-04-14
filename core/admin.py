from django.contrib import admin

from .models import Dish
from .models import Category
# Register your models here.
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("dish_name","spice_level","has_chestnuts","is_vegetarian","price","dish_category")
    list_filter = ("dish_name","spice_level","has_chestnuts","is_vegetarian","price","dish_category")
    search_fields = ("dish_name","spice_level","has_chestnuts","is_vegetarian","price","dish_category")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass