"""ejercicio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from ejercicio.views import index
from ejercicio.views import iniciar
from ejercicio.views import contacts
from ejercicio.views import servicio
from ejercicio.views import index
from ejercicio.views import solicitar_asesoria
from ejercicio.views import cliente
from ejercicio.views import profesional
from ejercicio.views import adminstrador
from ejercicio.views import perfil_cliente
from ejercicio.views import planificar_visita
from ejercicio.views import crear_capacitacion
from ejercicio.views import crear_caso_asesoria
from ejercicio.views import ingresar_ac_mejora
from ejercicio.views import Reportar_accidente
from ejercicio.views import RevisarCheklist

from core import views
from django.conf.urls import url

from core.views import registro_cliente
from core.views import login
from core.views import reporte_accidente
from core.views import crear_capacitacio
from core.views import crear_check
from core.views import planificar_visit
from core.views import ingresar_act
from core.views import verificar_contrato
from core.views import enviar_formulario



urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('iniciar/iniciar.html',iniciar,name='iniciar'),
    path('contacts.html',contacts),
    path('iniciar.html',servicio),
    path('iniciar/index.html',index),
    path('cliente.html',cliente,name='cliente'),
    path('profesional.html',profesional),
    #path('index.html',profesional),
    path('iniciar/registro/', views.registro_cliente, name='registro_cliente'),
    path('iniciar/login', views.login_view, name='login_view'),
    path('consulta_cliente/', views.consulta_clientes, name='consulta_clientes'),
    path('consulta_profesional/', views.consulta_profesional, name='consulta_profesional'),
    path('adminstrador.html',adminstrador),
    path('solicitar_asesoria.html',solicitar_asesoria),
    path('perfil_cliente.html',perfil_cliente,name='perfil_cliente'),
    path('crear_capacitacion.html',crear_capacitacion),
    path('planificar_visita.html/',views.planificar_visita,name='planificar_visita'),
    path('crear_caso_asesoria.html',views.crear_caso_asesoria,name='crear_caso_asesoria'),
    path('ingresar_ac_mejora.html/',views.ingresar_ac_mejora,name='ingresar_ac_mejora'),
    path('solicitar_asesoria/', views.solicitar_asesorias, name='solicitar_asesorias'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('eliminar_cliente/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('agregar_profesional/', views.agregar_profesional, name='agregar_profesional'),
    path('eliminar_profesional/<int:profesional_id>/', views.eliminar_profesional, name='eliminar_profesional'),
    path('Reportar_accidente.html',Reportar_accidente,name='reportar_accidente'),
    path('reporte_accidente', views.reporte_accidente, name='reporte_accidente'),
    path('planificar_visit', views.planificar_visit, name='planificar_visit'),
    path('crear_capacitacio', views.crear_capacitacio, name='crear_capacitacio'),
    path('ingresar_act', views.ingresar_act, name='ingresar_act'),
    path('agregar_asesoria/', views.agregar_asesoria, name='agregar_asesoria'),
    path('crear_check', views.crear_check, name='crear_check'),
    path('RevisarCheklist', views.RevisarCheklist, name='RevisarCheklist'),
    path('ingresar_chek', views.ingresar_chek, name='ingresar_chek'),
    path('datosreportes/', views.datosreportes, name='datosreportes'),
    path('agregar_contrato/', views.agregar_contrato, name='agregar_contrato'),
    path('verificar_contrato/<str:nombre_usuario>/', views.verificar_contrato, name='verificar_contrato'),
    path('enviar_formulario/', enviar_formulario, name='enviar_formulario'),
    

    

    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

