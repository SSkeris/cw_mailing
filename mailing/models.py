from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Mailing(models.Model):
    """"""
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
