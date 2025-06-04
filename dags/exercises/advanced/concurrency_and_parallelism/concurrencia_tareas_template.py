"""
Desafío: Concurrencia de Tareas con Límite

Crea un DAG que lance varias tareas en paralelo, pero limita la concurrencia máxima a 2 tareas activas al mismo tiempo usando la configuración del DAG. Cada tarea debe simular trabajo con un sleep y mostrar su inicio y fin en consola.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time

# TODO: Define la función tarea_paralela(numero_tarea: int) -> None

# TODO: Define la variable cantidad_tareas

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG con max_active_tasks=2

# TODO: Crea las tareas usando un ciclo y PythonOperator

# TODO: Establece las dependencias si es necesario

Funciones sugeridas:
- tarea_paralela(numero_tarea: int) -> None

Variables sugeridas:
- cantidad_tareas: int
- tareas_paralelas: list
"""
