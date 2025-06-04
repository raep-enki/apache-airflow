"""
Desafío: Pools y Queues desde Configuración

Crea un DAG que defina varias tareas, cada una asignada a un pool y una queue diferente, usando una lista de configuración en el código. Simula trabajo en cada tarea y muestra en consola el pool y la queue usados.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time

# TODO: Define la función tarea_pool_queue(nombre_tarea: str, pool: str, queue: str) -> None

# TODO: Define la lista configuracion_tareas con diccionarios que incluyan nombre, pool y queue

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG

# TODO: Crea las tareas usando un ciclo y PythonOperator, asignando pool y queue

# TODO: Establece las dependencias si es necesario

Funciones sugeridas:
- tarea_pool_queue(nombre_tarea: str, pool: str, queue: str) -> None

Variables sugeridas:
- configuracion_tareas: list
- tareas_configuradas: list
"""
