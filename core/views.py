from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from core.models import Dish

# Create your views here.
def index(request):

    dishes = Dish.objects.all()

    return render(request,'index.html',{"dishes": dishes})

def about(request):

    return render(request,'about.html')