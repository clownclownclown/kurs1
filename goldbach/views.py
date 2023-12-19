from django.shortcuts import render, redirect
from .forms import *
from .utils import *
from .models import *


def show_main_page(request):
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            calculation_result = goldbach(int(cleaned_data['source_number']))
            if int(cleaned_data['source_number']) % 2 != 0:
                form.add_error(None, 'Ошибка калькуляции: Число должно быть чётным')
                return render(request, 'goldbach/index.html', {'form': form})
            Calculation.objects.create(source_number=cleaned_data['source_number'],
                                       first_calculated_number=calculation_result[0],
                                       second_calculated_number=calculation_result[1],
                                       calculation_method='Перебор')
            return render(request, 'goldbach/postcalculation.html', {'form': form,
                                                                     'first_calculation': calculation_result[0],
                                                                     'second_calculation': calculation_result[1],
                                                                     'source_number': int(
                                                                         cleaned_data['source_number'])})
    else:
        form = CalculationForm()
        return render(request, 'goldbach/index.html', {'form': form})

def show_history_page(request):
    previous_calculations = Calculation.objects.all()
    return render(request, 'goldbach/history.html', {'history': previous_calculations})

def delete_history(request):
    Calculation.objects.all().delete()
    previous_calculations = Calculation.objects.all()
    return redirect('history')
