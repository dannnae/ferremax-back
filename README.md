# FERREMAS BACKEND

Back de proyecto Ferremas

## Requisitos

- MySQL
- Django 4.1.7
- Python 3.10.0

## Pasos

1. Crear entorno virtual `python -m venv env`
2. Activar scripts `env/Scripts/activate`
3. Instalar dependencias con el comando `pip install -r requirements.txt`
4. Crear archivo `my.cnf`
5. Crear archivo `.env`
6. Crear migraciones `python manage.py makemigrations`
7. Correr migracions `python manage.py migration`
8. Crear productos ejemplos `python manage.py crear_productos`

## Para ejecutar el proyecto
1. Correr server con el comando:
   `python manage.py runserver`

## Documentación API
- URL: `http://127.0.0.1:8000/swagger`
