"""
Desafío: Tareas Dinámicas desde Configuración

Crea un DAG que lea una lista de tareas desde una Variable de Airflow llamada "config_tareas" (en formato JSON) y genere dinámicamente una tarea por cada elemento, mostrando el nombre de la tarea en consola.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime

# TODO: Define la función mostrar_nombre_tarea(nombre: str) -> None

# TODO: Obtén la lista de nombres desde Variable.get('config_tareas', ...)

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG

# TODO: Crea las tareas dinámicamente usando un ciclo y PythonOperator

# TODO: Establece las dependencias si es necesario

Funciones sugeridas:
- mostrar_nombre_tarea(nombre: str) -> None

Variables sugeridas:
- lista_nombres: list
- tareas_dinamicas: list
"""
