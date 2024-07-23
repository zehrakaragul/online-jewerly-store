
from django.contrib import admin
from .models import  Shop , Category #, Slider


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("kategorismi", "urun_sayisi")
    prepopulated_fields = {"slug": ("kategorismi",), }

    def urun_sayisi (self , obj):
        return obj.shop_set.count()


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("urunismi", "fiyat","fiyatbirim", "isActive","category_list")
    prepopulated_fields = {"slug":("urunismi",),}
    search_fields = ("urunismi", "marka")
    list_filter = ( "kategoriler","isActive")

    def category_list(self , obj):
        html=" "
        for category in obj.kategoriler.all():
            html+=category.kategorismi+ "/"
        return html

#admin.site.register(Slider)

admin.site.site_header = 'Yönetim'
admin.site.index_title = 'Yönetim Paneli'