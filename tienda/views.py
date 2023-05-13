from django.conf import settings
from django.shortcuts import render, redirect
from .models import Account, Producto

from .forms import ProductoForm, RegistrationForm

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse

def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated: 
    	return HttpResponse("Ya tienes tu sesión activada cómo: " + str(user.email))
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect('main')
            
        else:
            context['registration_form'] =form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'registro.html', context)

def crearProducto(request):
    user = request.user
    if user.is_authenticated and user.is_admin:
        formCatalogo=ProductoForm(request.POST or None, request.FILES or None)
        if formCatalogo.is_valid():
            formCatalogo.save()
            return redirect('crearProducto')
        return render(request, 'crearProducto.html', {'formCatalogo':formCatalogo})
    else:
        return HttpResponse("No tiene permisos para acceder a esta página")

def main(request):
    productos = Producto.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(productos,6)
        productos = paginator.page(page)
    except:
        raise Http404


    data = {
        'entity': productos,
        'paginator': paginator
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
            # messages.success(request, 'Bienvenido {}'.format(user.email))
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
   

def editar(request, id):
    pedidos = Pedido.objects.get(idPedido=id)
    formulario = PedidoForm(request.POST or None, instance=pedidos)
    if formulario.is_valid and request.POST:
        formulario.save()
        return redirect('pedidos')
    return render(request, 'pedidos/crear.html', {'formulario':formulario})

def dashboardMain(request):
    user = request.user
    productos = Producto.objects.all()
    if user.is_authenticated and user.is_admin:
        return render(request, 'dashboard/main.html', {"productos": productos })
    else:
        return HttpResponse("No tiene permisos para acceder a esta página")
    

