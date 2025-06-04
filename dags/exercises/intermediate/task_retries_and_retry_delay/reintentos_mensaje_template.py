"""
Desafío: Reintentos con Mensaje Personalizado

Crea un DAG con una tarea que falle aleatoriamente y configure los reintentos y el retraso entre reintentos usando default_args. La tarea debe imprimir un mensaje personalizado en consola cada vez que falle o tenga éxito.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random

# TODO: Define la función tarea_con_reintentos(mensaje: str) -> None

# TODO: Define la variable mensaje_reintentos

# TODO: Configura los argumentos por defecto (default_args) con retries y retry_delay

# TODO: Crea el objeto DAG

# TODO: Crea la tarea tarea_reintentos usando PythonOperator

# TODO: Establece las dependencias si es necesario

Funciones sugeridas:
- tarea_con_reintentos(mensaje: str) -> None

Variables sugeridas:
- mensaje_reintentos: str
- tarea_reintentos: PythonOperator
"""
