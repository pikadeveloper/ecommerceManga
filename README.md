Se necesita realizar la configuración inicial
Pasos a seguir

Acceder Mysql SHELL

mysql -u root -p

Nuestra base de datos se llama EcommerceManga

Crear una base de datos
create database name;

Eliminar una base de datos
drop database name;

Dentro del directorio del proyecto
ejecutar el comando pip install -r requirements.txt

Comprobar si existen carpetas de pycache y migrations, eliminarlas para no tener conflictos entre archivos

Ejecutar comandos

python manage.py makemigrations tienda

python manage.py makemigrations carts

python manage.py migrate

Para realizar pruebas crear el super usuario
python manage.py createsuperuser

seguir pasos de la consola