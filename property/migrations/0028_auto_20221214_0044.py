# Generated by Django 2.2.24 on 2022-12-13 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0027_auto_20221214_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='flat_likes', to='property.Flat', verbose_name='Кто лайкнул'),
        ),
    ]
