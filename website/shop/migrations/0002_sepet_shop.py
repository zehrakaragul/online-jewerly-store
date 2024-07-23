# Generated by Django 4.1.3 on 2024-05-02 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sepet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=50)),
                ('urunismi', models.CharField(max_length=50)),
                ('aciklama', models.TextField()),
                ('resimUrl', models.CharField(max_length=200)),
                ('fiyat', models.IntegerField()),
                ('fiyatbirim', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=50)),
                ('urunismi', models.CharField(max_length=50)),
                ('aciklama', models.TextField()),
                ('resimUrl', models.CharField(max_length=200)),
                ('fiyat', models.IntegerField()),
                ('fiyatbirim', models.CharField(max_length=10)),
                ('isActive', models.BooleanField()),
                ('slug', models.SlugField(default='', unique=True)),
                ('kategoriler', models.ManyToManyField(to='shop.category')),
            ],
        ),
    ]