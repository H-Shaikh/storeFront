# Generated by Django 4.2.4 on 2023-08-16 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_price_product_unit_price_product_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['first_name', 'last_name']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title']},
        ),
    ]
