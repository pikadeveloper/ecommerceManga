from django.contrib import admin
from .models import Producto, User, Pedido
# Register your models here.

admin.site.register(User)
admin.site.register(Pedido)
admin.site.register(Producto)