from django.contrib import admin
from .models import *

class DocenteAdmin(admin.ModelAdmin):
    #listar los datos que quiero mostrar
    list_display = (
        'last_name',
        'first_name',
        'materia',
        'id',
    )
    #campo de búsqueda
    search_fields = ('last_name', 'first_name', 'materia')
    #listado de filtros al costado
    list_filter = ('materia',)

class NoDocenteAdmin(admin.ModelAdmin):
    #listar los datos que quiero mostrar
    list_display = (
        'last_name',
        'first_name',
        'oficina',
        'id',
    )
    #campo de búsqueda
    search_fields = ('last_name', 'first_name', 'oficina')
    #listado de filtros al costado
    list_filter = ('oficina',)

#Registro los dos modelos
admin.site.register(Docente, DocenteAdmin)
admin.site.register(NoDocente, NoDocenteAdmin)
