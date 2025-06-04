"""
Desafío: Mostrar Fecha de Ejecución Actual (catchup desactivado)

Crea un DAG que imprima la fecha de ejecución (execution_date) únicamente para la fecha actual, desactivando el catchup. El DAG debe tener una sola tarea que muestre la fecha en consola.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# TODO: Define la función mostrar_fecha_actual(**context) -> None

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG con catchup desactivado

# TODO: Crea la tarea tarea_mostrar_fecha usando PythonOperator

# TODO: Establece las dependencias si es necesario

Funciones sugeridas:
- mostrar_fecha_actual(**context) -> None

Variables sugeridas:
- tarea_mostrar_fecha: PythonOperator
"""
