from django import forms
from .models import *
from .validators import *

class CalculationForm(forms.Form):
    source_number = forms.IntegerField(label='Исходное число')

