# Generated by Django 3.0.4 on 2020-09-02 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_auto_20200902_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='img/product/baby.jpg', upload_to='img/product/'),
        ),
    ]
