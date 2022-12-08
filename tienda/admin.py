from django.contrib import admin
from .models import Producto, Account, Pedido
# Register your models here.

admin.site.register(Account)
admin.site.register(Pedido)
admin.site.register(Producto)