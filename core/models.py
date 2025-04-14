from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

import core.models


class Category(models.Model):
    category_name = models.CharField(max_length=30,null=False,blank=False)
    def __str__(self):
        return self.category_name
    class Meta:
        db_table = "categories"
        verbose_name_plural = "Categories"

class Dish(models.Model):
    objects = None
    dish_name = models.CharField(verbose_name="Meal",max_length=255,null=False,blank=False)
    spice_level = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    has_chestnuts = models.BooleanField(default=False,null=False,blank=False)
    is_vegetarian = models.BooleanField(default=False,null=False,blank=False)
    price = models.DecimalField(validators=[MinValueValidator(0)],max_digits=5,default=9999,decimal_places=2)
    dish_category = models.ForeignKey("core.Category",on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.dish_name

    class Meta:
        db_table = "dishes"
        verbose_name_plural = "Dishes"
