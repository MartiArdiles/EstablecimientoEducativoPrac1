from typing import ContextManager
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy
from .models import Docente
from .models import NoDocente
from .forms import DocenteForm
from .forms import NoDocenteForm

# Create your views here.

class DocenteListView(ListView):
    model = Docente
    template_name = "registro/listar-materias.html"
    context_object_name = 'lista'


class NoDocenteListView(ListView):
    model = NoDocente
    template_name = "registro/listar-oficinas.html"
    context_object_name = 'lista'

#Listar docentes por apellido
class DocenteListViewAll(ListView):
    model = Docente
    template_name = "registro/list_all_docentes.html"
    ordering = 'last_name'
    context_object_name = 'lista'
    #paginación de 4 elementos
    paginate_by = 4

#Listar el docente buscado por palabra clave (apellido)
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Docente.objects.filter(
            last_name__icontains = palabra_clave
        )
        return lista

#Listar no docentes por apellido
class NoDocenteListViewAll(ListView):
    model = NoDocente
    template_name = "registro/list_all_nodocentes.html"
    ordering = 'last_name'
    context_object_name = 'lista'
    #paginación de 4 elementos
    paginate_by = 4

#Listar el no docente buscado por palabra clave (apellido)
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = NoDocente.objects.filter(
            last_name__icontains = palabra_clave
        )
        return lista

class NoDocenteListViewBuscar(ListView):
    model = NoDocente
    template_name = "registro/buscar_nodocente.html"
    context_object_name = 'lista'

#Listar el docente buscado por palabra clave (apellido)
#Para obtener info de la base, para html uso el método GET
class DocenteListViewBuscar(ListView):
    model = Docente
    template_name = "registro/buscar_docente.html"
    context_object_name = 'lista'

#Devuelve el detalle del docente según su id
class DocenteDetailView(DetailView):
    model = Docente
    template_name = "registro/docente_detalle.html"
    context_object_name = 'docente_detalle'

class NoDocenteDetailView(DetailView):
    model = NoDocente
    template_name = "registro/nodocente_detalle.html"
    context_object_name = 'nodocente_detalle'

#Crear un nuevo docente
#Para meter info a la base, en el html uso el método POST
class DocenteCreateView(CreateView):
    model = Docente
    template_name = "registro/crear_docente.html"
    form_class = DocenteForm

    #Si la modificación se hace con éxito, la app se pasa a llamar éxito
    success_url = reverse_lazy('registro_app:listar-todo-docentes')

    #Método para mostrar nombre completo
    def form_valid(self, form):
        #Todo lo que genere, se guarda acá previamente
        docente = form.save(commit=False)
        docente.full_name = docente.first_name + ' ' + docente.last_name
        docente.save()
        return super(DocenteCreateView, self).form_valid(form)

#Crear un nuevo no docente
#Para meter info a la base, en el html uso el método POST
class NoDocenteCreateView(CreateView):
    model = NoDocente
    template_name = "registro/crear_nodocente.html"
    form_class = NoDocenteForm

    #Si la modificación se hace con éxito, la app se pasa a llamar éxito
    success_url = reverse_lazy('registro_app:listar-todo-nodocentes')

    #Método para mostrar nombre completo
    def form_valid(self, form):
        #Todo lo que genere, se guarda acá previamente
        nodocente = form.save(commit=False)
        nodocente.full_name = nodocente.first_name + ' ' + nodocente.last_name
        nodocente.save()
        return super(NoDocenteCreateView, self).form_valid(form)

#Modificar datos de un docente
class DocenteUpdateView(UpdateView):
    model = Docente
    template_name = "registro/modificar_docente.html"
    form_class = DocenteForm

    success_url = reverse_lazy('registro_app:listar-todo-docentes')

    def form_valid(self, form):
        #Todo lo que genere, se guarda acá previamente
        docente = form.save(commit=False)
        docente.full_name = docente.first_name + ' ' + docente.last_name
        docente.save()
        return super(DocenteUpdateView, self).form_valid(form)

#Modificar datos de un no docente
class NoDocenteUpdateView(UpdateView):
    model = NoDocente
    template_name = "registro/modificar_nodocente.html"
    form_class = NoDocenteForm

    success_url = reverse_lazy('registro_app:listar-todo-nodocentes')

    def form_valid(self, form):
        #Todo lo que genere, se guarda acá previamente
        nodocente = form.save(commit=False)
        nodocente.full_name = nodocente.first_name + ' ' + nodocente.last_name
        nodocente.save()
        return super(NoDocenteUpdateView, self).form_valid(form)

#Eliminar un docente
class DocenteDeleteView(DeleteView):
    model = Docente
    template_name = "registro/eliminar_docente.html"
    success_url = reverse_lazy('registro_app:listar-todo-docentes')

#Eliminar un no docente
class NoDocenteDeleteView(DeleteView):
    model = NoDocente
    template_name = "registro/eliminar_nodocente.html"
    success_url = reverse_lazy('registro_app:listar-todo-nodocentes')






#Se cumple con lo que es SCRUD: search, create, read, update y delete


class VistaPrincipal(TemplateView):
    template_name = "index.html"



