# Generated by Django 4.1 on 2022-09-14 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_date',
            field=models.DateField(default=datetime.date(2022, 9, 14)),
        ),
    ]