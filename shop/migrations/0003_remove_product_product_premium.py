# Generated by Django 4.0.6 on 2022-08-13 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_product_premium'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_premium',
        ),
    ]
