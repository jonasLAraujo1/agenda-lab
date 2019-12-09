class Agenda():
	def __init__(self,professor,disciplina,laboratorio,soft_uso,horario,turno,dia_semana):
		self.professor = professor
		self.disciplina = disciplina
		self.laboratorio = laboratorio
		self.soft_uso = soft_uso
		self.horario = horario
		self.turno = turno
		self.dia_semana = dia_semana

class Horario():
	def __init__(self,fim_uso,inicio_uso):
		self.fim_uso = fim_uso
		self.inicio_uso = inicio_uso
class Vagas():
	"""docstring for ClassName"""
	def __init__(self,laboratorio,turno,intervalo,status):
		self.laboratorio = laboratorio
		self.turno = turno
		self.intervalo = intervalo
		self.status = status

		
		
		