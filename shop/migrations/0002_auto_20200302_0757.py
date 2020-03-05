# Generated by Django 3.0.3 on 2020-03-02 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='../static/img/logo-img.png', upload_to='products/<built-in function id>/'),
        ),
    ]
