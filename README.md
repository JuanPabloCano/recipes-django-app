Trabajo final curso Django

Para correr este proyecto utilice los siguientes comandos:
* pip install -r requirements.txt
* python manage.py makemigrations
* python manage.py sqlmigrate - **nombre de la app + numero del archivo migrations** -> python manage.py sqlmigrate app 0001

La base de datos utilizada es MySQL, en el archivo settings cambiar la contraseña de la base de datos por la local.

Para crear un nuevo chat room dentro de la app, se debe hacer desde el admin
