
class Horarios():
	def __init__(self,intervalo,turno,status):
		self.intervalo = intervalo
		self.turno = turno
		self.status = status

class Local():
	"""docstring for ClassName"""
	def __init__(self,nome,dia_semana,horario_alocado):
		self.nome = nome
		self.dia_semana = dia_semana
		self.horario_alocado = horario_alocado


		
class Agenda():
	def __init__(self,solicitante,dias,local_solicitado,aulas,observacoes):
		
		self.solicitante = solicitante
		self.dias=dias
		self.local_solicitado = local_solicitado
		self.aulas = aulas
		self.observacoes = observacoes	
		
		