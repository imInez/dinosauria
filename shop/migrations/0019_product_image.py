# Generated by Django 3.0.4 on 2020-08-02 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20200802_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='../static/img/logo-img-light-green.png', upload_to='img/product'),
        ),
    ]
