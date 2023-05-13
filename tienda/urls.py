from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('usuario/registro', views.register_view, name='registro'),
    path('usuario/login', views.login_view, name='login'),
    path('usuario/logout', views.logout_view, name='logout'),
    path('crearProducto', views.crearProducto, name='crearProducto'),
    path('dashboard/', views.dashboardMain, name='dashboardMain'),
   
]