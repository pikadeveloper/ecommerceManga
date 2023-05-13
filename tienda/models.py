from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Los usuarios deben tener una dirección de correo electrónico")
        if not username:
            raise ValueError("Los usuarios deben tener un usuario")
            
        user = self.model(
            email=self.normalize_email(email),
            username= username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password = password,
            username= username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email= models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_join = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=60, blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS= ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Pedido(models.Model):
    idPedido = models.IntegerField(primary_key=True, verbose_name='pedido',default=0)
    idComprador = models.IntegerField(verbose_name='idCliente')
    pedidoDate = models.DateTimeField(verbose_name='fechaPedido')
    estado = models.TextField(max_length=20, verbose_name='estadoPedido')
    precio = models.IntegerField(verbose_name='precio')

    def __int__(self):
        resultado="pedido: "+self.idPedido+" - idCliente: "+self.idComprador+" - Fecha de Pedido: "+self.pedidoDate+" - Estado Pedido : "+self.estado+" - Precio: "+self.precio
        return resultado

    def save(self, *args, **kwargs):
        pedidos= Pedido.objects.all()
        if pedidos.exists() and self._state.adding:
            last_pedido = pedidos.latest('pedido')
            self.pedido = int(last_pedido.pedido) + 1
            #self.idPedido = self.idPedido + 1
        super().save(*args, **kwargs)  # Call the "real" save() method.

class Carrito(models.Model):
    idCart = models.IntegerField(primary_key=True, verbose_name='idCart')
    productoId = models.IntegerField(verbose_name='productoId')
    

    def __int__(self):
        resultado="Carrito: "+self.idCart+" - producto agregado: "+self.productoId
        return resultado

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name='idProducto')
    nombreProducto = models.CharField(max_length=255,verbose_name='nombre')
    autor = models.CharField(max_length=255,verbose_name='autor')
    precioProducto = models.IntegerField(verbose_name='precio')
    imagen= models.ImageField(upload_to="productos")
    stock = models.IntegerField(verbose_name='stock')

    def __str__(self):
        resultado="nombre: "+self.nombreProducto+ " - autor: "+self.autor+" - precio: "+str(self.precioProducto)
        return resultado

#class User(AbstractUser):
    #email= models.EmailField('email',primary_key=True, unique=True)
    #idUsuario = models.IntegerField(verbose_name='idUsuario')
    #nombre = models.TextField(max_length=20,verbose_name='nombre')
    #apellido = models.TextField(max_length=20,verbose_name='apellido')
    #USERNAME_FIELD='email'
    #REQUIRED_FIELDS= ['username']
    #password = models.CharField(max_length=32,verbose_name='password')
    #direccion = models.TextField(max_length=255, verbose_name='direccion')
    #direccionFactura = models.TextField(max_length=255,verbose_name='direccionFactura')
    
    #def __int__(self):
    #    resultado="id: "+self.idUsuario+" - Nombre: "+self.nombre+" - Apellido: "+self.nombre+" - Email: "+self.email+" - Contraseña : "+self.password+" - Direccion envio: "+self.direccion+" - Direccion de factura: "+self.direccionFactura
    #   return resultado


#def idIncrement():
    #largest = Pedido.objects.all().order_by('idPedido').last()
    #if not largest:
    #    return 0
    #return largest.idPedido + 1
    