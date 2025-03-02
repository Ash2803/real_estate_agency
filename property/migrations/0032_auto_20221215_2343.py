# Generated by Django 2.2.24 on 2022-12-15 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0031_auto_20221215_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]
