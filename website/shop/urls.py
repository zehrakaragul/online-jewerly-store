from django.urls import path
from . import views

#http://127.0.0.1:8000/client  =>anasayfa
#http://127.0.0.1:8000/client/home  =>anasayfa
#http://127.0.0.1:8000/client/makyaj  =>makyaj

urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search , name="search"),
    path('favori', views.favori, name="favori"),
    path('sepet', views.sepet, name="sepet"),
    path('<slug:slug>',views.detaylar , name="urun_detaylar"),
    path('kategori/<slug:slug>', views.getShopByCategory ,name= 'shops_by_category'),


]
