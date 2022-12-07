# Generated by Django 2.2.24 on 2022-12-07 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20221207_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apartment', to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
    ]
