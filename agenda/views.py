from django.shortcuts import render, redirect
from .forms import *
from .entidades.agenda import Agenda, Horario
from .services import agenda_services
# Create your views here.
def mostrar_form(request):
	if request.method =="POST":
		formulario = FormAgenda(request.POST)
		if formulario.is_valid():
			professor = formulario.cleaned_data["professor"]
			disciplina = formulario.cleaned_data["disciplina"]
			laboratorio = formulario.cleaned_data["laboratorio"]
			soft_uso = formulario.cleaned_data["soft_uso"]
			turno = formulario.cleaned_data["turno"]
			dia_semana = formulario.cleaned_data["dia_semana"]

			nova_agenda=Agenda(professor=professor,disciplina=disciplina,
				laboratorio=laboratorio,soft_uso=soft_uso,
				horario=0,turno=turno,dia_semana=dia_semana)			
			return redirect('form_etapa2',nova_agenda)
			
	formulario = FormAgenda()
	return render(request, 'agenda/pagina_cadastro.html',{"formulario":formulario})

def form_etapa2(request,agenda_nova):
	if request.method == "POST":
		formulario_horario = FormHorario(request.POST)
		if formulario_horario.is_valid():
			inicio=formulario_horario.cleaned_data["inicio_uso"]
			fim=formulario_horario.cleaned_data["fim_uso"]
			novo_horario=Horario(fim_uso=fim,inicio_uso=inicio)
	#formulario = FormAgenda()
	formulario_horario=FormHorario()
	return render(request, 'agenda/cadastro_etapa2.html',{"formulario_horario":formulario_horario})



def agenda1(request):
	valores=agenda_services.retornar_agenda()
	agenda_services.cadastro_vagas()	
	return render(request,'agenda/agenda_bootstrap.html',{"valores":valores})

def agenda2(request):
	valores=agenda_services.retornar_agenda(2)	
	return render(request,'agenda/agenda_bootstrap.html',{"valores":valores})

def agenda3(request):
	valores=agenda_services.retornar_agenda(3)	
	return render(request,'agenda/agenda_bootstrap.html',{"valores":valores})