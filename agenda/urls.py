from django.contrib import admin
from django.urls import path
from .views import *
from .entidades.agenda import Agenda
urlpatterns = [
    path('agenda/manha',agenda1,name="agenda1"),
    path('agenda/tarde',agenda2,name="agenda2"),
    path('agenda/noite',agenda3,name="agenda3"),
    path('pagina_cadastro_2',form_etapa2,name="form_etapa2"),
    # path('agenda_2',ver_agenda_2,name="ver_agenda_2"),
    # path('agenda_bootstrap',agenda_bootstrap,name="agenda_bootstrap"),
    path('pagina_cadastro',mostrar_form,name="mostrar_form"),
]
