# Generated by Django 4.1.3 on 2022-11-21 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_prod_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_date',
            field=models.DateField(default=datetime.date(2022, 11, 21)),
        ),
    ]
