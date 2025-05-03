from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from unicodedata import category

from core.models import Dish,Category
from .forms import DishForms
# Create your views here.

def index(request):
    search_query = request.GET.get('q','')
    category = request.GET.get('category','')
    spice_level = request.GET.get('spice_level','')
    has_chestnuts = request.GET.get('has_chestnuts','')
    is_vegetarian = request.GET.get('is_vegetarian','')
    dishes = Dish.dishes.all().select_related('dish_category')
    if search_query:
        dishes = dishes.filter(Q(dish_name__icontains=search_query))
    if category:
        dishes = dishes.filter(dish_category_id=category)
    if spice_level:
        dishes = dishes.filter(spice_level=spice_level)
    if has_chestnuts:
        dishes = dishes.filter(has_chestnuts=has_chestnuts)
    if is_vegetarian:
        dishes = dishes.filter(is_vegetarian=is_vegetarian)
    categories = Category.objects.all()
    return render(request,'index.html',{
        "dishes": dishes,
        'categories': categories,
        'search_query': search_query,
        'category': category,
        'spice_level': spice_level,
        'has_chestnuts': has_chestnuts,
        'is_vegetarian': is_vegetarian,
    })
#class DishListView(ListView):
#    model = Dish
#    template_name = ("index.html")


def about(request):

    return render(request,'about.html')

def dish_expand(request,slug):

   dish_detail = get_object_or_404(Dish,slug=slug,in_stock=True)
   return render(request,'dish_expand.html',{"dish_detail": dish_detail})
#class DishDetailView(DetailView):
#   model = Dish
#    template_name = "dish_expand.html"
def category_set(request,category_slug = None):
    category = get_object_or_404(Category, slug=category_slug)
    dish_list = Dish.objects.filter(dish_category=category)
    return render(request,'category_set.html',{"category": category,"dish_list": dish_list})

def add_dish(request):

    if request.method == "POST":
        form = DishForms(request.POST)

        if form.is_valid():
            form.save()
            return redirect("core:index")
    else:
        form = DishForms()

    return render(request,"add_dish.html",{"form" : form})
