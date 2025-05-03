"""
URL configuration for begin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core.views import index
from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
#from core.views import DishListView,DishDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.url',namespace='core')),
    #path('dish_expand/<int:dish_pk>', include('core.url',namespace='core'), name="dish_expand"),
    #path('',DishListView.as_view(),name="index"),
    path('about/',include('core.url',namespace='core')),
    path('dish/',include('core.url',namespace='core')),
    path("add_dish/",include("core.url",namespace='core')),
    path("search/",include("core.url",namespace='core')),
    path('basket/',include('basket.urls',namespace='basket')),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)