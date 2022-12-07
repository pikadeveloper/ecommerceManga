from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email= models.EmailField('email',primary_key=True, unique=True)
    idUsuario = models.IntegerField(verbose_name='idUsuario')
    nombre = models.TextField(max_length=20,verbose_name='nombre')
    apellido = models.TextField(max_length=20,verbose_name='apellido')
    USERNAME_FIELD='email'
    REQUIRED_FIELDS= ['username']
    password = models.CharField(max_length=32,verbose_name='password')
    direccion = models.TextField(max_length=255, verbose_name='direccion')
    direccionFactura = models.TextField(max_length=255,verbose_name='direccionFactura')
    
    def __int__(self):
        resultado="id: "+self.idUsuario+" - Nombre: "+self.nombre+" - Apellido: "+self.nombre+" - Email: "+self.email+" - Contraseña : "+self.password+" - Direccion envio: "+self.direccion+" - Direccion de factura: "+self.direccionFactura
        return resultado


class Pedido(models.Model):
    idPedido = models.IntegerField(primary_key=True, verbose_name='pedido')
    idComprador = models.IntegerField(verbose_name='idCliente')
    pedidoDate = models.DateTimeField(verbose_name='fechaPedido')
    estado = models.TextField(max_length=20, verbose_name='estadoPedido')
    precio = models.IntegerField(verbose_name='precio')

    def __int__(self):
        resultado="pedido: "+self.idPedido+" - idCliente: "+self.idComprador+" - Fecha de Pedido: "+self.pedidoDate+" - Estado Pedido : "+self.estado+" - Precio: "+self.precio
        return resultado

class Carrito(models.Model):
    idCart = models.IntegerField(primary_key=True, verbose_name='idCart')
    productoId = models.IntegerField(verbose_name='productoId')
    

    def __int__(self):
        resultado="Carrito: "+self.idCart+" - producto agregado: "+self.productoId
        return resultado

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='idProducto')
    nombreProducto = models.CharField(max_length=255,verbose_name='nombre')
    autor = models.CharField(max_length=255,verbose_name='autor')
    precioProducto = models.IntegerField(verbose_name='precio')
    imagen= models.ImageField(upload_to="productos")
    stock = models.IntegerField(verbose_name='stock')

    def __str__(self):
        resultado="nombre: "+self.nombreProducto+ " - autor: "+self.autor+" - precio: "+self.precioProducto
        return resultado