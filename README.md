# intranet
Aplicación Básica para funcionalidades como intranet

## Instalación

* Crear un entorno virtual de python 3 (usando virtualenvwrapper sería así)

```
	mkvirtualenv intranet --python=/usr/bin/python3
```

* Instalar los requisitos

```
	pip install -r requirements.txt
```

* Realizar las migraciones

```
	python manage.py makemigrations
	python manage.py makemigrations base
	python manage.py makemigrations users
```

* Correr el proyecto

```
	python manage.py runserver
```