# Generated by Django 3.2.6 on 2021-09-15 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_pro_kind'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pro_kind',
        ),
    ]
