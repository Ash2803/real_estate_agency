# Generated by Django 2.2.24 on 2022-12-07 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_alter_flat_owners_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to='property.Flat', verbose_name='Кто лайкнул'),
        ),
    ]
