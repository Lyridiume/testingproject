from django.urls import path

from core.views import index
#from core.views import DishListView,DishDetailView
from core.views import about
from core.views import dish_expand
from core.views import add_dish
from core.views import category_set
app_name = "core"

urlpatterns = [
    #path('',DishListView.as_view(),name="index"),
    path('',index,name="index"),
    path('about/',about,name="about"),
    #path('dish_expand/<int:dish_pk>',DishDetailView.as_view(),name="dish_expand"),
    path('dish/<slug:slug>/',dish_expand,name="dish_expand"),
    path('add_dish/',add_dish,name="add_dish"),
    path('search/<slug:category_slug>/',category_set,name="category_set"),
]