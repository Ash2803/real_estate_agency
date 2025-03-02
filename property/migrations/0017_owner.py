# Generated by Django 2.2.24 on 2022-12-09 21:34

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_parse_numbers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('owner_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца')),
                ('owner_flats', models.ManyToManyField(related_name='flats', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
