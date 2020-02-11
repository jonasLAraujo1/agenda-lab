from django.db import models

# Create your models here.


class Horarios(models.Model):
	
	# STATUS_CHOICES = (
	# 	("1", "Livre"),
	# 	("2", "Em Uso")
	# )
	intervalo = models.CharField(max_length = 14, null=False, blank=False)
	# turno = models.CharField(max_length = 1, choices = TURNO_CHOICES, null=False, blank=False)
	# dia_semana = models.CharField(max_length = 1, choices = DIA_SEMANA_CHOICES, null=False, blank=False)
	# status = models.CharField(max_length = 1, choices = STATUS_CHOICES, null=False, blank=False)
	def __str__(self):
		return self.intervalo

class Dia(models.Model):
	dia_semana = models.CharField(max_length = 25, null=False, blank=False)
	def __str__(self):
		return self.dia_semana

class Local(models.Model):
	nome = models.CharField(max_length = 120, null=False, blank=False)
	def __str__(self):
		return self.nome
	
class Agenda(models.Model): #relacionamento 1 para muitos (um usuario pode fazer varios agendamentos, 
# em varios horarios e em varios turnos)
	solicitante= models.CharField(max_length = 120, null=False, blank=False)
	local_solicitado = models.ForeignKey("Local", on_delete=models.CASCADE)
	dias=models.ForeignKey("Dia", on_delete=models.CASCADE)
	aulas=models.ManyToManyField(Horarios)
	observacoes= models.CharField(max_length = 150, null=True, blank=True)