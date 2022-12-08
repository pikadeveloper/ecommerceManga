from django.shortcuts import render, redirect
from .models import Account, Producto
from .forms import ProductoForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout



def registro(request):
    #usuario=Usuario.objects.all()

    return render(request, 'registro.html', {'Users': Account})

def crearProducto(request):
    formCatalogo=ProductoForm(request.POST or None, request.FILES or None)
    if formCatalogo.is_valid():
        formCatalogo.save()
        return redirect('crearProducto')
    return render(request, 'crearProducto.html', {'formCatalogo':formCatalogo})

def main(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'principal.html', data)

def login_view(request):
    if request.method == 'POST': #Se condiciona el método para obtener valores
        username = request.POST.get('email')  #se ocupa diccionario POST, se obtienen los inputs desde el login
        password = request.POST.get('password')
        
        user = authenticate(request , email=username, password=password)
        print(user)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.email))
            return redirect('main')
        else:
            messages.error(request, 'Correo o Contraseña no validos')
        #if user:
            #pass
    user=Account.objects.all()
    #
    return render(request, 'login.html', {'User': Account})

def logout_view(request):
    logout(request)
    messages.success(request, "Sessión cerrada exitosamente")
    return redirect('login')
   
