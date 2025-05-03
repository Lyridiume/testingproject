from enum import unique

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
class DishManager(models.Manager):
    def get_queryset(self):
        return super(DishManager, self).get_queryset().filter(in_stock=True)

class Category(models.Model):
    objects = None
    category_name = models.CharField(max_length=30,null=False,blank=False,db_index=True)
    slug = models.SlugField(max_length=255,null=True,unique=True)

    def get_absolute_url(self):
        return reverse('core:category_set', args=[self.slug])
    def __str__(self):
        return self.category_name
    class Meta:
        db_table = "categories"
        verbose_name_plural = "Categories"

class Dish(models.Model):
    dish_name = models.CharField(verbose_name="Meal",max_length=255,null=False,blank=False)
    dish_description = models.TextField(blank=True)
    dish_image = models.ImageField(upload_to="images/",null=True)
    spice_level = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    has_chestnuts = models.BooleanField(default=False,null=False,blank=False)
    is_vegetarian = models.BooleanField(default=False,null=False,blank=False)
    price = models.DecimalField(validators=[MinValueValidator(0)],max_digits=5,default=9999,decimal_places=2)
    in_stock = models.BooleanField(default=True,null=False)
    slug = models.SlugField(max_length=255,null=True,unique=True)
    dishes = DishManager()
    dish_category = models.ForeignKey("core.Category",related_name='dish',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.dish_name

    def get_absolute_url(self):
        return reverse('core:dish_expand',args=[self.slug])

    class Meta:
        db_table = "dishes"
        verbose_name_plural = "Dishes"
