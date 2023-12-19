from django.utils.timezone import now

from django.db import models

class Calculation(models.Model):
    calculation_time = models.DateTimeField('Время расчёта', default=now())
    source_number = models.IntegerField('Изначальное число')
    first_calculated_number = models.IntegerField('Первое число суммы')
    second_calculated_number = models.IntegerField('Второе число суммы')
    calculation_method = models.CharField('Метод вычисления', max_length=256)

    def __str__(self):
        return str(self.source_number)

    class Meta:
        verbose_name = "Расчёт"