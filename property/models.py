from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    BOOL_CHOICES = (
        (True, 'Да'),
        (False, 'Нет'),
        (None, 'Неизвестно')
    )
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)
    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)
    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    new_building = models.BooleanField(choices=BOOL_CHOICES,
                                       default=None,
                                       blank=True,
                                       null=True,
                                       verbose_name="Новостройка"
                                       )
    likes = models.ManyToManyField("Flat", blank=True, related_name="owners_likes", verbose_name='Кто лайкнул')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200)
    phonenumber = models.CharField(max_length=20, verbose_name='Номер владельца', db_index=True)
    pure_phonenumber = PhoneNumberField("Нормализованный номер владельца",
                                        blank=True,
                                        db_index=True
                                        )
    flats = models.ManyToManyField('Flat',
                                   related_name='owners',
                                   verbose_name='Квартиры в собственности',
                                   blank=True
                                   )

    def __str__(self):
        return self.name


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="Кто жаловался",
                             related_name='claims'
                             )
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE,
                             null=True,
                             related_name='claims',
                             verbose_name="Квартира, на которую пожаловались"
                             )
    complaint = models.TextField(blank=True, verbose_name="Текст жалобы")
