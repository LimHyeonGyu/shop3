# Generated by Django 3.2.6 on 2021-09-15 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_pro_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pro_status',
            field=models.CharField(choices=[('f', 'Fruit'), ('p', 'Phone'), ('c', 'Computer')], max_length=1, null=True),
        ),
    ]
