# Generated by Django 3.0.3 on 2020-03-02 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200302_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='../static/img/logo-img.png', upload_to='img/product'),
        ),
    ]
