from django import forms
from .models import *

class DateInput(forms.DateInput):
	input_type = 'date'


class TimeInput(forms.TimeInput):
	input_type = 'time'


class FormAgenda(forms.ModelForm):
	local_solicitado=forms.ModelChoiceField(queryset=Local.objects.all())
	dia_semana=forms.ModelChoiceField(queryset=Dia.objects.all())
	aulas=forms.ModelMultipleChoiceField(queryset=Horarios.objects.all())

	class Meta:
		model = Agenda
		fields = ['solicitante','local_solicitado','dia_semana','aulas','observacoes']
		

# class FormHorario(forms.ModelForm):
# 	#inicio_uso = forms.ModelChoiceField(queryset=Vagas.objects.all())
# 	class Meta:
# 		model = Horarios
# 		fields = ['turno']

# class FormLocal(forms.ModelForm):
# 	#inicio_uso = forms.ModelChoiceField(queryset=Vagas.objects.all())
# 	local_solicitado=forms.ModelChoiceField(queryset=Local.objects.all())
# 	class Meta:
# 		model = Agenda
# 		fields = ['local_solicitado']

# class FormDia(forms.ModelForm):
# 	#inicio_uso = forms.ModelChoiceField(queryset=Vagas.objects.all())
# 	dia_semana=forms.ModelChoiceField(queryset=Horarios.objects.all())
# 	class Meta:
# 		model = Agenda
# 		fields = ['local_solicitado']
# 				