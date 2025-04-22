from django.urls import path
from setuptools.extern import names

from core.url import app_name
from . import views
app_name = 'basket'
urlpatterns = [
    path('',views.basket_general,name='basket_general'),
    path('add_dish/',views.basket_add,name='basket_add'),
    path('delete_dish/',views.basket_delete,name='basket_delete')
]