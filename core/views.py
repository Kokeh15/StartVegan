from django.shortcuts import render, redirect
from .models import Pro, Usuario
from .forms import ProForm
from django.http import HttpResponseRedirect
from django.contrib import messages 

# Create your views here.


def home(request):

    return render(request, 'core/home.html')


def almuerzo(request):
    return render(request, 'core/Almuerzo.html')

def cena(request):
    return render(request, 'core/Cena.html')

def Desayuno(request):
    return render(request, 'core/Desayuno.html')

#listados
def listacena(request):
    productoss = Pro.objects.all()
    data = {
        'productoss':productoss
    }

    
    return render(request, 'core/listacena.html',data)


def listadesayuno(request):
    productoss = Pro.objects.all()
    data = {
        'productoss':productoss
    }
    return render(request, 'core/listadesayuno.html',data)

def listproductos(request):
    productoss = Pro.objects.all()
    data = {
        'productoss':productoss
    }
    return render(request, 'core/listaproductos.html',data)


def agregarcena(request):

    data = {
        'form':ProForm()
    }

    if request.method == 'POST':
        formulario = ProForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
        data['form'] = formulario



    return render(request, 'core/agregarcena.html',data)


def eliminarcena(request,id):

    productoss = Pro.objects.get(id=id)
    try:
        productoss.delete()
        mensaje = "se ha eliminado"
        messages.success(request, mensaje)
    except: 
        mensaje = "No se ha podido eliminar"
        messages.error(request, mensaje)
    
    return redirect('lista_cena')

#Paginas
def contacto(request):
    return render(request, 'core/Contacto.html')



def registrarse(request):
    return render(request, 'core/registrarse.html')


def modificarprod(request, id):
    productoss = Pro.objects.get(id=id)
    data = {
        'form': ProForm(instance=productoss)
    }

    if request.method == 'POST':
        formulario = ProForm(data=request.POST, instance= productoss)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado"
            data['form'] = formulario

    return render(request, 'core/modificarproductos.html', data)


def login(request):
    if request.method == "GET":
        return render(request, 'core/login.html', {"msg": ""})
    nombre = request.POST.get("nombre", "")
    contrasena = request.POST.get("contrasena", "")
    print("---")
    print("Nombre: "+nombre)
    print("PWD: "+contrasena)
    print("----")
    usuario = Usuario.objects.filter(nombre=nombre)
    print(usuario[0].contrasenia)
    if len(usuario) == 0 or usuario[0].contrasenia != contrasena:
        return render(request, 'core/login.html', {"msg": "Error al iniciar sesión"})
    else:
        return HttpResponseRedirect( '/')