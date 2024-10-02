# Clonación del Repositorio y Configuración de una Aplicación Django
# crud de productos en url admin proporcionada por django

## Paso 1: Clonar el Repositorio

Para clonar el repositorio, abre tu terminal y ejecuta el siguiente comando:

```bash
git clone  https://github.com/Soinekro/crud_products_django.git
cd crud_products_django
```

## Paso 2: Crear y Activar un Entorno Virtual

debes tener instalado [python 3](https://www.python.org/downloads) y [pip](https://pip.pypa.io/)

```bash
python -m pip install Django
```


## Paso 3: verificar django instalado 

```bash 
python -m django --version
``` 

## Paso 4: Configurar la Base de Datos

Asegúrate de tener configurada la [base de datos](https://docs.djangoproject.com/en/5.1/topics/install/#get-your-database-running) en el archivo `settings.py` de tu proyecto Django. Por ejemplo:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

## Paso 5: Aplicar Migraciones

Ejecuta las migraciones para configurar la base de datos:

```bash
python manage.py migrate
```

## Paso 6: Crear un Superusuario

Crea un superusuario para acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```

## Paso 7: Ejecutar el Servidor de Desarrollo

Finalmente, ejecuta el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

Ahora puedes acceder a tu aplicación Django en `http://127.0.0.1:8000/`.

## Paso 8: Acceder al Panel de Administración

Para acceder al panel de administración, ve a `http://127.0.0.1:8000/admin/` e ingresa con las credenciales del superusuario que creaste.

¡Y eso es todo! Ahora tienes tu aplicación Django clonada y en funcionamiento.


## Resumen de Aprendizaje

Aprendí a utilizar el framework Django mediante el [tutorial de creación de encuestas](https://docs.djangoproject.com/en/5.1/intro/tutorial01/) de la documentación oficial de Django. Este tutorial me proporcionó una base sólida sobre cómo funciona Django y cómo desarrollar aplicaciones web con este framework.

Además, utilicé el internet para buscar soluciones a algunos problemas que encontré debido a mi inexperiencia con el framework. La comunidad y los recursos en línea fueron de gran ayuda para superar estos obstáculos.

También utilicé inteligencia artificial para el desarrollo del proyecto, lo cual me permitió optimizar el proceso y resolver dudas de manera más eficiente.
