from django.http import HttpResponse
from ckeditor.fields import RichTextField
from shop.models import  Shop , Category
from django.shortcuts import get_object_or_404,render
from django.core.paginator import Paginator

# Create your views here.
def index1(request):
   #list comphension alt satırda yapılan şeyin adı
    urunler = Shop.objects.filter(isActive=True).order_by("urunismi")
    kategoriler = Category.objects.all()
   # sliders= Slider.objects.filter(is_active=True)

    paginator = Paginator(urunler,5)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, 'pages/index1.html', {
        'categories': kategoriler,
        'urunler' :  urunler,
        'page_obj': page_obj,
        #'sliders' : sliders
    })
#def detaylar(request , slug):
#    shop = get_object_or_404(Shop , slug=slug)
 #   context = {
  #'urun': shop
   # }
    #return render(request, 'pages/detaylar.html', context)

def iletisim(request):
    return render(request, 'pages/iletisim.html')