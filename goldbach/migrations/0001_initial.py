# Generated by Django 4.2.8 on 2023-12-11 21:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calculation_time', models.DateTimeField(default=datetime.datetime(2023, 12, 11, 21, 2, 2, 425687, tzinfo=datetime.timezone.utc), verbose_name='Время расчёта')),
                ('source_number', models.IntegerField(verbose_name='Изначальное число')),
                ('first_calculated_number', models.IntegerField(verbose_name='Первое число суммы')),
                ('second_calculated_number', models.IntegerField(verbose_name='Второе число суммы')),
                ('calculation_method', models.CharField(max_length=256, verbose_name='Метод вычисления')),
            ],
            options={
                'verbose_name': 'Расчёт',
            },
        ),
    ]