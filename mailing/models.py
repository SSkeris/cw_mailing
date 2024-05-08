from datetime import timedelta, time
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    """Клиент"""
    FIO = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(max_length=150, verbose_name='Почта', unique=True)
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.FIO} {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('FIO',)


class Mailing(models.Model):
    """Рассылка и её параметры"""
    DAILY = "Раз в день"
    WEEKLY = "Раз в неделю"
    MONTHLY = "Раз в месяц"

    PERIODICITY_CHOICES = [
        (DAILY, "Раз в день"),
        (WEEKLY, "Раз в неделю"),
        (MONTHLY, "Раз в месяц"),
    ]

    CREATED = 'Создана'
    STARTED = 'Запущена'
    COMPLETED = 'Завершена'

    STATUS_CHOICES = [
        (COMPLETED, "Завершена"),
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
    ]

    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default=CREATED, verbose_name='Статус')
    periodicity = models.CharField(max_length=150, choices=PERIODICITY_CHOICES,
                                   default=DAILY, verbose_name='Периодичность')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата окончания')
    clients = models.ManyToManyField(Client, verbose_name='Клиенты для рассылки')

    def __str__(self):
        return f'{self.name} {self.status}, время работы: {self.start_date} - {self.end_date}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('name',)
