# Generated by Django 3.0.3 on 2020-03-26 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200302_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='../static/img/logo-img-light-green.png', upload_to='img/product'),
        ),
    ]
