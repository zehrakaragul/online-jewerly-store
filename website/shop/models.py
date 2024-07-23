from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.
from django.contrib.auth.models  import User
class Category(models.Model):
    kategorismi= models.CharField(max_length=70)
    slug= models.SlugField(default="", null=False, unique=True, db_index=True,max_length=70)

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural= 'Kategoriler'

    def __str__(self):
        return f"{self.kategorismi}"

class Shop(models.Model):
    marka = models.CharField(max_length=50)
    urunismi=models.CharField(max_length=50 )
    aciklama = RichTextField()
    resimUrl = models.CharField(max_length=200)
    fiyat = models.IntegerField()
    fiyatbirim= models.CharField(max_length=10)
    isActive =models.BooleanField()
    slug = models.SlugField(default="", null= False, unique=True, db_index=True )
    kategoriler = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural= 'Ürünler'

    def __str__(self):
        return f"{self.urunismi}"





