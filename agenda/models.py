from django.db import models

# Create your models here.

class Agenda(models.Model):
	LABS_CHOICES = (
        ("1", "Laboratório de Redes de Computadores"),
        ("2", "Laboratório de Informática"),
        ("3", "Laboratório de Arquitetura de Computadores")

	)
	TURNO_CHOICES = (
        ("1", "Manhã"),
        ("2", "Tarde"),
        ("3", "Noite")
	)
	DIA_SEMANA_CHOICES = (
		("1", "Segunda-Feira"),
		("2", "Terça-Feira"),
		("3", "Quarta-Feira"),
		("4", "Quinta-Feira"),
		("5", "Sexta-Feira"),
	)

	disciplina = models.CharField(max_length = 120, null = False, blank=False)
	laboratorio = models.CharField(max_length = 1, choices = LABS_CHOICES, null=False, blank=False)
	professor = models.CharField(max_length = 120, null = False, blank=False)
	soft_uso = models.CharField(max_length = 120, null = True, blank=True)
	horario = models.OneToOneField("Horario", on_delete = models.CASCADE)

	turno = models.CharField(max_length = 1, choices = TURNO_CHOICES, null=False, blank=False)
	dia_semana = models.CharField(max_length = 1, choices = DIA_SEMANA_CHOICES, null=False, blank=False)


class Horario(models.Model):
	fim_uso = models.TimeField(null=False, blank=False)
	inicio_uso = models.TimeField(null=False, blank=False)
	
class Vagas(models.Model):
	STATUS_CHOICES = (
        ("1", "Livre"),
        ("2", "Ocupado")
	)
	
	laboratorio= models.CharField(max_length = 120, null=False, blank=False)
	turno = models.CharField(max_length = 120, null=False, blank=False)
	intervalo=models.CharField(max_length = 120, null=False, blank=False)
	status=models.CharField(max_length = 1, choices = STATUS_CHOICES, null=False, blank=False)