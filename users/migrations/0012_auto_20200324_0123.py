# Generated by Django 3.0.3 on 2020-03-24 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200324_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipmentaddress',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]
