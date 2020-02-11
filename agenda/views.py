from django.shortcuts import render, redirect
from .forms import *
from .entidades.agenda import *
from .services import agenda_services
# Create your views here.
def mostrar_form(request):
	if request.method =="POST":
		formulario = FormAgenda(request.POST)
		if formulario.is_valid():
			solicitante = formulario.cleaned_data["solicitante"]
			local_solicitado = formulario.cleaned_data["local_solicitado"]
			dias = formulario.cleaned_data["dia_semana"]
			aulas = formulario.cleaned_data["aulas"]
			observacoes = formulario.cleaned_data["observacoes"]
			nova_agenda=Agenda(solicitante=solicitante,local_solicitado=local_solicitado,
				dias=dias,aulas=aulas,observacoes=observacoes)
			agenda_services.salvar_agenda(nova_agenda)			
			return redirect('agenda1')
			
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
	# agenda_services.salvar_dados()
	# vagas_services.cadastro_vagas()
	horarios=agenda_services.retornar_horarios()
	estrutura=agenda_services.retornar_agenda()	
	return render(request,'agenda/agenda.html',{'estrutura':estrutura})#,{"valores":valores})

def agenda2(request):
	valores=agenda_services.horarios()	
	return render(request,'agenda/agenda.html',{"valores":valores,"range":range(5)})

def agenda3(request):
	valores=agenda_services.retornar_agenda(3)	
	return render(request,'agenda/agenda.html',{"valores":valores})
def criarHorarios(request):
	agenda_services.salvar_horario()	
	return render(request,'agenda/agenda.html')