# Generated by Django 3.0.4 on 2020-08-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_product_image_blob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_blob',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
