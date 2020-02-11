from ..models import Vagas
def cadastro_vagas():
	for lab in ("Laboratório de Redes de Computadores",
		"Laboratório de Informática",
		"Laboratório de Arquitetura de Computadores"):
		for i in {1:"07:00 as 07:50",2:"07:50 as 08:40",3:"08:40 as 09:30",4:"09:50 as 10:40",5:"10:40 as 11:30",6:"11:30 as 12:20"}.values():
			Vagas.objects.create(laboratorio=lab,turno="Manhã",intervalo=i)
