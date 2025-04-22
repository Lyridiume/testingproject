from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from basket.basket import Basket
from core.models import Dish


# Create your views here.
def basket_general(request):
    return render(request,'basket/general.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        dish_id = int(request.POST.get('dishid'))
        dish_qty = int(request.POST.get('dishqty'))
        dish = get_object_or_404(Dish,id=dish_id)
        basketqty = basket.__len__()
        basket.add_dish(dish=dish,dish_qty=dish_qty)
        response = JsonResponse({'qty': basketqty})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'delete':
        dish_id = int(request.POST.get('dishid'))
        basket.delete(dish=dish_id)