# Generated by Django 2.2.24 on 2022-12-11 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0023_auto_20221212_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to='property.Owner', verbose_name='Кто лайкнул'),
        ),
    ]
