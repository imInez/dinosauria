# Generated by Django 3.0.3 on 2020-03-26 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_order_payment_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created']},
        ),
    ]
