from django import forms
from .models import *

class DateInput(forms.DateInput):
	input_type = 'date'


class TimeInput(forms.TimeInput):
	input_type = 'time'


class FormAgenda(forms.ModelForm):
	class Meta:
		model = Agenda
		fields = ['professor','disciplina','laboratorio',
		'soft_uso','turno','dia_semana']
		

class FormHorario(forms.ModelForm):
	#inicio_uso = forms.ModelChoiceField(queryset=Vagas.objects.all())
	class Meta:
		model = Horario
		fields = '__all__'
		