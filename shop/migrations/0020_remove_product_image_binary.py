# Generated by Django 3.0.4 on 2020-08-03 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_binary',
        ),
    ]
