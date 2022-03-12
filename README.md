# Biblioteca API

> django y django rest framework

> Api para servir a la aplicacion de biblioteca construida en react

## Build Setup

```bash
# instalar un entorno virtual de python 3.x
$ python3 -m venv virtualenv

# instalar dependencias
$ pip install -r requirements.txt

# correr las migracions -  
$ python manage.py makemigrations users 
$ python manage.py makemigrations books 
$ python manage.py migrate

# crear un superusuario para acceder al admin
$ python manage.py createsuperuser

# serve with hot reload at localhost:8000
$ python manage.py runserver

# cargar datos al modelo de libros
$ desde el administrador de django dirigirse al modelo de libros
$ e importar los datos books.json al modelo





```

