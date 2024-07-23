import json

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404, render, redirect
from .models import Shop, Category
from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.
from ckeditor.fields import RichTextField

def index(request):
   #list comphension alt satırda yapılan şeyin adı
    urunler = Shop.objects.filter(isActive=True).order_by("urunismi")
    kategoriler = Category.objects.all()
   # sliders= Slider.objects.filter(is_active=True)

    paginator = Paginator(urunler,15)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)


    return render(request, 'shop/index.html', {
        'categories': kategoriler,
        'urunler' :  urunler,
        'page_obj': page_obj,
        #'sliders' : sliders
    })
def search(request):
    if "q" in request.GET and request.GET["q"] !="":
        q= request.GET["q"]
        urunler = Shop.objects.filter( isActive=True,urunismi__contains=q).order_by("marka")

    else:
        return redirect("")
    paginator = Paginator(urunler, 9)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, 'shop/list.html', {
      'page_obj': page_obj,
 })

def favori(request):
    return render(request, 'favori.html')


def sepet(request):
  return render(request, 'sepet.html')




def detaylar(request , slug):
    shop = get_object_or_404(Shop , slug=slug)
    context = {
        'urun': shop
    }
    return render(request, 'detaylar.html', context)

def getShopByCategory(request , slug):
    urunler = Shop.objects.filter(kategoriler__slug = slug, isActive=True).order_by("marka")
    kategoriler= Category.objects.all()

    paginator = Paginator(urunler , 9)
    page= request.GET.get('page',1)
    page_obj = paginator.page(page)




    return render(request,'shop/index.html',{
        'categories': kategoriler,
        'page_obj': page_obj,
        'seciliKategori': slug

    })
