"""
Desafío: Plantilla Jinja para Nombre Personalizado

Crea un DAG que utilice una plantilla Jinja para mostrar un mensaje personalizado con el nombre del usuario y la fecha de ejecución ({{ ds }}) en consola. El nombre debe estar definido como variable en el código y la fecha debe ser pasada usando la plantilla.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# TODO: Define la función mostrar_mensaje(nombre: str, fecha: str) -> None

# TODO: Define la variable nombre_usuario

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG

# TODO: Crea la tarea tarea_mensaje_nombre usando PythonOperator y pasando nombre_usuario y '{{ ds }}'

# TODO: Establece las dependencias si es necesario

Funciones sugeridas:
- mostrar_mensaje(nombre: str, fecha: str) -> None

Variables sugeridas:
- nombre_usuario: str
- tarea_mensaje_nombre: PythonOperator
"""
