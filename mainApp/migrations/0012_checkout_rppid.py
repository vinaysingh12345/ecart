# Generated by Django 4.1.7 on 2023-05-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0011_buyer_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='rppid',
            field=models.CharField(default='', max_length=30),
        ),
    ]
