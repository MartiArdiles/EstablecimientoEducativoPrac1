from django import forms
from django.forms import widgets
from django.forms.formsets import formset_factory
from .models import Docente
from .models import NoDocente

class DocenteForm(forms.ModelForm):

    class Meta:
        model = Docente
        fields = (
            'first_name',
            'last_name',
            'materia',
            'age',
            'avatar',
        )

class NoDocenteForm(forms.ModelForm):

    class Meta:
        model = NoDocente
        fields = (
            'first_name',
            'last_name',
            'oficina',
            'age',
            'avatar',
        )