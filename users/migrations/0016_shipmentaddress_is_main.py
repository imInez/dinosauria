# Generated by Django 3.0.3 on 2020-03-30 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20200330_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipmentaddress',
            name='is_main',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
