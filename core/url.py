from django.urls import path

from core.views import index
from core.views import about
app_name = "core"

urlpatterns = [
    path('',index,name="index"),
    path('about/',about,name="about")
]