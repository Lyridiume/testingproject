from django.contrib import admin

from .models import Dish
from .models import Category
# Register your models here.
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("dish_name","dish_description","spice_level","has_chestnuts","is_vegetarian","price","dish_category","slug","in_stock")
    list_filter = ("dish_name","dish_description","spice_level","has_chestnuts","is_vegetarian","price","dish_category","slug","in_stock")
    search_fields = ("dish_name","dish_description","spice_level","has_chestnuts","is_vegetarian","price","dish_category","slug","in_stock")
    prepopulated_fields = {'slug':('dish_name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','slug')
    prepopulated_fields = {'slug':('category_name',)}