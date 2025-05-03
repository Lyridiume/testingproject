from django import forms

from .models import Dish

class DishForms(forms.ModelForm):

    class Meta:
        model = Dish
        fields = "__all__"