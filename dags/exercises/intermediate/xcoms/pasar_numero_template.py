"""
Desafío: Pasar un Número entre Tareas con XCom

Crea un DAG con dos tareas: la primera debe enviar un número aleatorio usando XCom y la segunda debe leer ese número y mostrarlo en consola.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import random

# TODO: Define la función enviar_numero_xcom(**context) -> None
# TODO: Define la función recibir_numero_xcom(**context) -> None

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG

# TODO: Crea las tareas tarea_enviar_numero y tarea_recibir_numero usando PythonOperator

# TODO: Establece las dependencias: enviar_numero >> recibir_numero

Funciones sugeridas:
- enviar_numero_xcom(**context) -> None
- recibir_numero_xcom(**context) -> None

Variables sugeridas:
- tarea_enviar_numero: PythonOperator
- tarea_recibir_numero: PythonOperator
"""
