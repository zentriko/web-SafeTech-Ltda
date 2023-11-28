from django import forms
from django.conf import settings
from core.models import Cliente
from core.models import Asesoria
from core.models import Reporte
from core.models import Capacitacion
from core.models import Visita
from core.models import Actividad
from core.models import Checklist


class ClienteForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput)
    #confirmar_contrasena = forms.CharField(widget=forms.PasswordInput, label='Repetir Contraseña')

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido','tipo_empresa','nombre_empresa','correo','usuario','contrasena']


class AsesoriaForm(forms.ModelForm):
    cliente_username = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Asesoria
        fields = ['tipo_asesoria', 'detalle', 'fecha_inicio','cliente_username']  # Asegúrate de incluir 'cliente_username' aquí


class ReporteForm(forms.ModelForm):


    class Meta:
        model = Reporte
        fields = ['numero','nombre_empresa', 'tipo','descripcion','fecha_creacion']

class CapacitacionForm(forms.ModelForm):


    class Meta:
        model = Capacitacion
        fields = ['nombre_empresa','tipo_cap', 'fecha', 'asistentes','material']


class VisitaForm(forms.ModelForm):


    class Meta:
        model = Visita
        fields = ['fecha_visita', 'resultado']

class ActividadForm(forms.ModelForm):


    class Meta:
        model = Actividad
        fields = ['estado','nombre_act','tipo_empresa','nombre_empresa','nombre_cliente','fecha']

class ChecklistForm(forms.ModelForm):


    class Meta:
        model = Checklist
        fields = ['titulo','descripcion','tipo_empresa']

