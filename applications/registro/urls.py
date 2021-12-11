from django.contrib import admin
from django.urls import path, include
from . import views

#Ponerle nombre a la app
app_name = 'registro_app'

urlpatterns = [
    path(
        'listar-todo-docentes/', 
    views.DocenteListViewAll.as_view(),
     name='listar-todo-docentes'
     ),

    path(
        'listar-todo-nodocentes/', 
    views.NoDocenteListViewAll.as_view(), 
    name='listar-todo-nodocentes'
    ),

    path(
        'buscar-por-apellido-nodocente/', 
    views.NoDocenteListViewBuscar.as_view(), 
    name= 'buscar-nodocentes'
    ),

    path(
        'buscar-por-apellido-docente/', 
    views.DocenteListViewBuscar.as_view(), 
    name= 'buscar-docentes'
    ),

    path(
        'docente_detalle/<pk>/',
     views.DocenteDetailView.as_view(), 
     name='docente_detalle'
    ),

    path(
        'nodocente_detalle/<pk>/',
     views.NoDocenteDetailView.as_view(), 
     name='nodocente_detalle'
    ),

    path(
        'crear_docente/',
    views.DocenteCreateView.as_view(),
    name='crear_docente'
    ),

    path(
        'crear_nodocente/',
    views.NoDocenteCreateView.as_view(),
    name='crear_nodocente'
    ),

    path('modificar_docente/<pk>/', 
    views.DocenteUpdateView.as_view(), 
    name='modificar_docente'
    ),

    path('modificar_nodocente/<pk>/', 
    views.NoDocenteUpdateView.as_view(), 
    name='modificar_nodocente'
    ),

    path('eliminar_docente/<pk>/', 
    views.DocenteDeleteView.as_view(), 
    name='eliminar_docente'
    ),

    path('eliminar_nodocente/<pk>/', 
    views.NoDocenteDeleteView.as_view(), 
    name='eliminar_nodocente'
    ),

    path('docente_detalle/<pk>/', 
    views.DocenteDetailView.as_view(), 
    name='docente_detalle'),

    path('nodocente_detalle/<pk>/', 
    views.NoDocenteDetailView.as_view(), 
    name='nodocente_detalle'),

    path('listar-materias/', 
    views.DocenteListView.as_view(), 
    name='listar-materias'),

    path('listar-oficinas/', 
    views.NoDocenteListView.as_view(), 
    name='listar-oficinas'),

    path('', 
    views.VistaPrincipal.as_view(), 
    name='index')
]