import smtplib
from email.message import EmailMessage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect,HttpResponse
from .forms import ClienteForm
from core.models import Cliente, Profesional, Administrador
from django.contrib.auth import login
from django.contrib.auth.models import User
from core.models import Cliente
from core.models import Visita
from core.models import Asesoriaprofesional
from core.models import Reporte
from core.models import Capacitacion
from core.models import Visita
from core.models import Contrato, Cliente
from core.models import Contrato
from core.models import Checklist
from core.models import Asesoria
from core.models import Cliente,Actividad
from django.core.exceptions import ObjectDoesNotExist
import json
from .forms import AsesoriaForm
from .forms import ReporteForm
from .forms import CapacitacionForm
from .forms import ChecklistForm
from .forms import VisitaForm
from .forms import ActividadForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def registro_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("iniciar")
            

        else:
            print(form.errors)
    else:
        form = ClienteForm()
        return render(request, "registrarse.html", {"form": form})




def login_view(request):
    usuario = None
    bandera_cliente = 0
    bandera_profesional = 0
    bandera_administrador = 0


    if request.method == 'POST':
        usuario_nombre = request.POST['usuario']  # Nombre del campo de entrada del nombre de usuario
        contrasena = request.POST['contrasena']  # Nombre del campo de entrada de la contraseña
        
        try:
            # Intenta buscar el usuario en los tres modelos
            usuario = Cliente.objects.get(usuario=usuario_nombre)
            if not (usuario is None):
                print("No entré al if none 1")
                bandera_cliente = 1
        except ObjectDoesNotExist:
    
            try:
                usuario = Profesional.objects.get(usuario=usuario_nombre)
                if not (usuario is None):
                    print("No entré al if none 1")
                    bandera_profesional = 1
            except ObjectDoesNotExist:
                try:
                    usuario = Administrador.objects.get(usuario=usuario_nombre)
                    if not (usuario is None):
                        print("No entré al if none 1")
                        bandera_administrador = 1
                except ObjectDoesNotExist:
                    usuario = None

        if usuario is not None and usuario.contrasena == contrasena:
            response_data = {
                'message': 'Inicio de sesión exitoso',
                'success': True
            }
            if bandera_cliente == 1:
                print("entre al if 1")
                response_data = {
                'message': 'Inicio de sesión : cliente',
                'success': True
        
                }
                return render(request, 'cliente.html')
              
              
            if bandera_profesional == 1:
                print("entre al if 2")
                response_data = {
                'message': 'Inicio de sesión : profesional',
                'success': True
                
                }
                return render(request, 'profesional.html')
                    

            if bandera_administrador == 1:
                print("entre al if 3")
                response_data = {
                'message': 'Inicio de sesión : administrador',
                'success': True
                
                }
                return render(request, 'adminstrador.html')
            
            
              
          
            
            # Redirige a la página principal 
        else:
            # El usuario no existe o la contraseña es incorrecta
            response_data = {
                'message': 'Credenciales incorrectas',
                'error': True
            }
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        

    #return render(request, 'index.html')

def consulta_clientes(request):
    clientes = Cliente.objects.all()
    print(clientes)  
    return render(request, 'consulta_cliente.html', {'clientes': clientes})

def consulta_profesional(request):
    profesional = Profesional.objects.all()
    print(profesional)  
    return render(request, 'consulta_profesional.html', {'profesional': profesional})
    
    


def planificar_visita(request):
    if request.method == 'POST':
        # Obtén datos del formulario 
        id_visita = request.POST.get('id_visita')
        fecha_visita = request.POST.get('fecha_visita')
        resultado = request.POST.get('resultado')
        detalle = request.POST.get('detalle')
        tipo_de_visita = request.POST.get('tipo_de_visita')
        asesoria_id = request.POST.get('asesoria_id') 
        cliente_id = request.POST.get('cliente_id')   
        profesional_id = request.POST.get('profesional_id')  

        # Crear una nueva instancia de Visita con los datos del formulario
        nueva_visita = Visita(id_visita=id_visita, fecha_visita=fecha_visita, resultado=resultado,
                              detalle=detalle, tipo_de_visita=tipo_de_visita,
                              asesoria_id=asesoria_id, cliente_id=cliente_id, profesional_id=profesional_id)

        # Guarda la nueva visita en la base de datos
        nueva_visita.save()

    # Obtén todos los objetos Visita 
    visita = Visita.objects.all()
    return render(request, 'planificar_visita.html', {'visita': visita})

def ingresar_ac_mejora(request):

    cliente = Cliente.objects.all()
    actividad = Actividad.objects.all()
    print(actividad)  
    return render(request, 'ingresar_ac_mejora.html', {'cliente': cliente,'actividad': actividad})



def solicitar_asesorias(request):
    if request.method == "POST":
        form = AsesoriaForm(request.POST)
        if form.is_valid():
            cliente_username = request.POST.get('cliente_username')  # Obtener el nombre de usuario del cliente del formulario
            cliente = Cliente.objects.get(usuario=cliente_username)  # Buscar el cliente por su nombre de usuario
            asesoria = form.save(commit=False)
            asesoria.cliente = cliente  # Establecer la relación con el cliente
            asesoria.save()
            return redirect("cliente")
        else:
            print(form.errors)
            return render(request, "solicitar_asesoria.html", {"form": form, "error": "El formulario no es válido"})
    else:
        form = AsesoriaForm()
        return render(request, "solicitar_asesoria.html", {"form": form})

def agregar_cliente(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')
        cliente = Cliente(nombre=nombre, apellido=apellido, usuario=usuario, contrasena=contrasena)
        cliente.save()
    return redirect('consulta_clientes')

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id_cliente=cliente_id)
    cliente.delete()
    return redirect('consulta_clientes')

def agregar_profesional(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')
        profesional = Profesional(nombre=nombre, apellido=apellido, usuario=usuario, contrasena=contrasena)
        profesional.save()
    return redirect('consulta_profesional')

def eliminar_profesional(request, profesional_id):
    profesional = get_object_or_404(Profesional, id_pro=profesional_id)
    profesional.delete()
    return redirect('consulta_profesional')

def reporte_accidente(request):
    if request.method == "POST":
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente")
        else:
            print(form.errors)
            return render(request, "Reportar_accidente.html", {"form": form})
    else:
        form = ReporteForm()
        return render(request, "Reportar_accidente.html", {"form": form})

def crear_capacitacio(request):
    if request.method == "POST":
        form = CapacitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/profesional.html")
        else:
            print(form.errors)
            return render(request, "crear_capacitacion.html", {"form": form})
    else:
        form = CapacitacionForm()
        return render(request, "crear_capacitacion.html", {"form": form})



def planificar_visit(request):
    if request.method == "POST":
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/profesional.html")
        else:
            print(form.errors)
            return render(request, "planificar_visita.html", {"form": form})
    else:
        form = VisitaForm()
        return render(request, "planificar_visita.html", {"form": form})

def ingresar_act(request):
    if request.method == "POST":
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/profesional.html")
        else:
            print(form.errors)
            return render(request, "ingresar_ac_mejora.html", {"form": form})
    else:
        form = ActividadForm()
        return render(request, "ingresar_ac_mejora.html", {"form": form})

def crear_caso_asesoria(request):
    asesoria = Asesoria.objects.all()
    print(asesoria)  
    return render(request, 'crear_caso_asesoria.html', {'asesoria': asesoria})



def crear_check(request):
    if request.method == "POST":
        form = ChecklistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/profesional.html")
        else:
            print(form.errors)
            return render(request, "planificar_visita.html", {"form": form})
    else:
        form = ChecklistForm()
        return render(request, "planificar_visita.html", {"form": form})


def agregar_asesoria(request):
    if request.method == "POST":
        detalle = request.POST.get('detalle')
        fecha = request.POST.get('fecha')
        cliente_id = request.POST.get('cliente_id')
        prioridad = request.POST.get('prioridad')
        tipo_asesoria = request.POST.get('tipo_asesoria')
        
        # Guardar la asesoría en la base de datos
        asesoriaprofesional = Asesoriaprofesional(detalle=detalle, fecha=fecha, cliente_id=cliente_id, prioridad=prioridad, tipo_asesoria=tipo_asesoria)
        asesoriaprofesional.save()
        
        # Enviar correo electrónico al cliente
        cliente = Cliente.objects.get(id_cliente=cliente_id)  # Obtener el cliente por su ID
        
        msg = EmailMessage()
        msg.set_content(f'Estimado {cliente.nombre},\n\nTu asesoría ha sido registrada con éxito.')
        msg['Subject'] = 'Asesoría Registrada'
        msg['From'] = 'diegomu2000@gmail.com'  
        msg['To'] = cliente.correo  # Usar el campo de correo electrónico del cliente
        
        try:
            # Establecer conexión con el servidor SMTP y enviar el correo
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Usar el servidor SMTP correspondiente
            server.starttls()
            server.login('diegomu2000@gmail.com', 'shtq rpgo qhaj guts')  
            server.send_message(msg)
            server.quit()
        except Exception as e:
            # Manejar errores si ocurren problemas al enviar el correo
            print(f'Error al enviar el correo: {e}')
        
    return redirect('/crear_caso_asesoria.html')

def consulta_check(request):
    checklist = Checklist.objects.all()
    print(checklist)  
    return render(request, 'consulta_cliente.html', {'checklist': checklist})

def RevisarCheklist(request):
    checklist = Checklist.objects.all()
    return render(request, 'RevisarCheklist.html', {'checklist': checklist})


def ingresar_chek(request):
    if request.method == "POST":
        form = ChecklistForm(request.POST)
        if form.is_valid():
            form.save()

            correo = form.cleaned_data['correo']

            msg = EmailMessage()
            msg.set_content(f'Estimado cliente,\n\nTu visita está registrada con éxito.')
            msg['Subject'] = 'Visita Registrada'
            msg['From'] = 'diegomu2000@gmail.com'  
            msg['To'] = correo  

            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('diegomu2000@gmail.com', 'shtq rpgo qhaj guts')
                server.send_message(msg)
                server.quit()
                return redirect("/profesional.html")
            except smtplib.SMTPException as e:
                print(f'Error al enviar el correo: {e}')
            except Exception as e:
                print(f'Otro error al enviar el correo: {e}')

            return redirect("/profesional.html")
        else:
            print(form.errors)
            return render(request, "planificar_visita.html", {"form": form})
    else:
        form = VisitaForm()
        return render(request, "planificar_visita.html", {"form": form})

def datosreportes(request):
    reporte = Reporte.objects.all()
    print(reporte)  
    return render(request, 'datosreportes.html', {'reporte': reporte})

def agregar_contrato(request):
    if request.method == "POST":
        cliente_username = request.POST.get('cliente_username')  # Obtener el nombre de usuario del cliente del formulario
        cliente = Cliente.objects.get(usuario=cliente_username)  # Buscar el cliente por su nombre de usuario
        nombre_usuario = request.POST.get('nombre_usuario')
        nombre_empresa= request.POST.get('nombre_empresa')
        tipo_empresa= request.POST.get('tipo_empresa')
        correo = request.POST.get('correo')
        tipo_suscripcion = request.POST.get('tipo_suscripcion')
        monto = request.POST.get('monto')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_termino = request.POST.get('fecha_termino')
        contrato = Contrato(cliente=cliente,nombre_usuario=nombre_usuario, nombre_empresa=nombre_empresa,tipo_empresa=tipo_empresa,correo=correo, tipo_suscripcion=tipo_suscripcion, monto=monto,fecha_inicio=fecha_inicio,fecha_termino=fecha_termino)
        contrato.save()
    return redirect('cliente')


def verificar_contrato(request, nombre_usuario):
    try:
        tiene_contrato = Contrato.objects.filter(nombre_usuario=nombre_usuario).exists()
        return JsonResponse({'tieneContrato': tiene_contrato})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt  # Se utiliza csrf_exempt para permitir solicitudes POST sin CSRF
def enviar_formulario(request):
    if request.method == 'POST':
        correo = request.POST.get('correo', '')
        archivo = request.FILES.get('archivo')
        print('Correo:', correo)
        print('Archivo:', archivo)

        if not correo or not archivo:
            return JsonResponse({'message': 'Por favor, complete todos los campos.'}, status=400)

        # Enviar correo electrónico con el archivo adjunto
        subject = 'Checklist Completo'
        message = 'Checklist Realizado con exito durante la visita'
        from_email = 'diegomu2000@gmail.com'  
        recipient_list = [correo]

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=recipient_list,
        )
        email.attach(archivo.name, archivo.read(), archivo.content_type)

        try:
            email.send(fail_silently=False)
            return redirect('/perfil_cliente.html') 
        except Exception as e:
            print(f'Error al enviar el correo: {e}')
            return JsonResponse({'message': 'Hubo un error al enviar el correo.'}, status=500)

    return JsonResponse({'message': 'Método no permitido'}, status=405)


