## Configuración para Iniciar el proyecto
Se debe tener instalado mysql y tener configurado una base de datos con el nombre "EcommerceManga"

### Pasos a seguir

- Acceder MySQL SHELL (usuario root liberado en condiciones de desarrollo)
``` mysql -u root -p ```

- Crear la base de datos 
```create database EcommerceManga;```

- Dentro del directorio, ejecutar el siguiente comando para instalar dependencias necesarias para la ejecución del proyhecto
```pip install -r requirements.txt```

Comprobar si existen carpetas de pycache y migrations, eliminarlas para no tener conflictos entre archivos

- Ejecutar los siguientes comandos de django para crear los modelos de datos e importarlos a MySQL
```
python manage.py makemigrations tienda

python manage.py makemigrations carts

python manage.py migrate
```
- Para realizar pruebas crear el super usuario
```python manage.py createsuperuser```

seguir pasos de la consola...

## Anexo:
- Eliminar una base de datos
```drop database name;```
