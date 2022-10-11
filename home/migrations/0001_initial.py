# Generated by Django 4.1.2 on 2022-10-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_products_image', models.ImageField(blank=True, upload_to='media')),
                ('products_image1', models.ImageField(blank=True, upload_to='media')),
                ('products_image2', models.ImageField(blank=True, upload_to='media')),
                ('products_image3', models.ImageField(blank=True, upload_to='media')),
                ('product_title', models.CharField(max_length=200)),
                ('product_desc', models.CharField(max_length=600)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='MainProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_image', models.ImageField(upload_to='media')),
                ('products_video', models.FileField(blank=True, upload_to='media/%y')),
                ('product_title', models.CharField(max_length=200)),
                ('product_desc', models.CharField(max_length=600)),
                ('product_spec1', models.CharField(max_length=600)),
                ('product_spec2', models.CharField(max_length=600)),
                ('product_spec3', models.CharField(max_length=600)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]