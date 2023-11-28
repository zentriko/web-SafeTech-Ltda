from django.db import models
from datetime import date
from django.conf import settings

# modelos aca



class Actividad(models.Model):
    id_actividad = models.AutoField( primary_key=True)
    nombre_cliente = models.CharField(max_length=20,null=True)
    estado = models.CharField(max_length=20)
    nombre_act = models.CharField(max_length=20)
    fecha = models.DateField()
    tipo_empresa = models.CharField(max_length=20,null=True)
    nombre_empresa = models.CharField(max_length=50, null=True)
    notificacion_enviada = models.BooleanField(default=False)
    administrador = models.ForeignKey('Administrador', on_delete=models.CASCADE,null=True)
    profesional = models.ForeignKey('Profesional', on_delete=models.CASCADE,null=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE,null=True)
    checklist = models.ForeignKey('Checklist', on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'actividad'

class Administrador(models.Model):
    id_administrador = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=20,unique=True)
    contrasena = models.CharField(max_length=50)

    class Meta:
        db_table = 'administrador'

class Asesoria(models.Model):
    id_asesoria = models.AutoField( primary_key=True)
    detalle = models.CharField(null=True,max_length=50)
    fecha_inicio = models.DateField(null=True, blank=True)  # Permite valores NULL
    tipo_asesoria = models.CharField(max_length=50)
    profesional = models.ForeignKey('Profesional', on_delete=models.CASCADE, null=True)
    reporte = models.ForeignKey('Reporte', on_delete=models.CASCADE, null=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'asesoria'

class Capacitacion(models.Model):
    id_capacitacion = models.AutoField( primary_key=True)
    nombre_empresa = models.CharField(max_length=50,null=True)
    tipo_cap = models.CharField(max_length=50)
    fecha = models.DateField()
    asistentes = models.CharField(max_length=50)
    material = models.CharField(max_length=500)
    asesoria = models.ForeignKey('Asesoria', on_delete=models.CASCADE,null=True)
    profesional = models.ForeignKey('Profesional', on_delete=models.CASCADE,null=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'capacitacion'

class Checklist(models.Model):
    id_checklist = models.AutoField( primary_key=True)
    titulo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=500)
    tipo_empresa = models.CharField(max_length=255, null=False, default='valor_por_defecto')
    ruta_documento = models.FileField(upload_to='documentos/')  # Aquí 'documentos/' es la carpeta donde se guardarán los archivos.
    visita = models.ForeignKey('Visita', on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'checklist'



class Cliente(models.Model):
    id_cliente = models.AutoField( primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipo_empresa = models.CharField(max_length=50, null=True)
    nombre_empresa = models.CharField(max_length=50, null=True)
    correo = models.CharField(max_length=128)
    usuario = models.CharField(max_length=20, unique=True, null=True)
    contrasena = models.CharField(max_length=20)
    fecha_registro = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Verifica  la fecha de registro 
        if not self.fecha_registro:
            self.fecha_registro = date.today()
        super().save(*args, **kwargs)

    
   

    class Meta:
        db_table = 'cliente'

class Contrato(models.Model):
    id_contrato = models.AutoField( primary_key=True)
    nombre_empresa = models.CharField(max_length=50,null=True)
    nombre_usuario = models.CharField(max_length=50,null=True)
    tipo_suscripcion = models.CharField(max_length=50,null=True)
    tipo_empresa = models.CharField(max_length=50,null=True)
    correo = models.CharField(max_length=50,null=True)
    fecha_inicio = models.DateField(max_length=50,null=True)
    fecha_termino = models.DateField(max_length=50,null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'contrato'

    def __str__(self):
        return f"Contrato de {self.nombre_usuario} ({self.cliente.usuario.username})"

class Profesional(models.Model):
    id_pro = models.AutoField( primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)
    usuario = models.CharField(max_length=20,unique=True)
    contrasena = models.CharField(max_length=20)

    class Meta:
        db_table = 'profesional'

class Reporte(models.Model):
    id_reporte = models.AutoField( primary_key=True)
    numero = models.IntegerField()
    titulo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    nombre_empresa = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=499)
    fecha_creacion = models.DateField()
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE,null=True)
    administrador = models.ForeignKey('Administrador', on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'reporte'

class Servicio(models.Model):
    id_servicio = models.AutoField( primary_key=True)
    tipo_servicio = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE)
    administrador = models.ForeignKey('Administrador', on_delete=models.CASCADE)

    class Meta:
        db_table = 'servicio'

class Visita(models.Model):
    id_visita = models.AutoField( primary_key=True)
    fecha_visita = models.DateField(null=True)
    resultado = models.CharField(max_length=499, null=True)
    asesoria = models.ForeignKey('Asesoria', on_delete=models.CASCADE,null=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE,null=True)
    profesional = models.ForeignKey('Profesional', on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'visita'


class Asesoriaprofesional(models.Model):
    id_asesoriapro = models.AutoField( primary_key=True)
    detalle = models.CharField(null=True,max_length=50)
    fecha = models.DateField(null=True, blank=True)  # Permite valores NULL
    prioridad = models.CharField(null=True,max_length=15)
    tipo_asesoria = models.CharField(max_length=50)
    profesional = models.ForeignKey('Profesional', on_delete=models.CASCADE, null=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'asesoriaprofesional'
