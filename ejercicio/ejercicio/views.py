from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def iniciar(request):
    return render(request, 'iniciar.html')



def contacts(request):
    return render(request, 'contacts.html')

def servicio(request):
    return render(request, 'iniciar.html')

def index(request):
    return render(request,'index.html')



def cliente(request):
    return render(request,'cliente.html')

def profesional(request):
    return render(request,'profesional.html')


def adminstrador(request):
    return render(request,'adminstrador.html')
    


def solicitar_asesoria(request):
    return render(request,'solicitar_asesoria.html')


    
def perfil_cliente(request):
    return render(request,'perfil_cliente.html')


def planificar_visita(request):
    return render(request,'planificar_visita.html')


def crear_capacitacion(request):
    return render(request,'crear_capacitacion.html')

def crear_caso_asesoria(request):
    return render(request,'crear_caso_asesoria.html')

def ingresar_ac_mejora(request):
    return render(request,'ingresar_ac_mejora.html')

def Reportar_accidente(request):
    return render(request,'Reportar_accidente.html')

def RevisarCheklist(request):
    return render(request,'RevisarCheklist.html')

    

