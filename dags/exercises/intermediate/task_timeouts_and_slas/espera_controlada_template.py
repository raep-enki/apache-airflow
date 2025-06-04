"""
Desafío: Espera Controlada con Timeout y SLA

Crea un DAG con una tarea que simule una espera (por ejemplo, usando sleep) y configura un tiempo límite de ejecución (execution_timeout) y un SLA. La tarea debe imprimir mensajes antes y después de la espera.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import time

# TODO: Define la función tarea_espera_controlada() -> None

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG

# TODO: Crea la tarea tarea_espera usando PythonOperator con execution_timeout y sla

# TODO: Establece las dependencias si es necesario

Funciones sugeridas:
- tarea_espera_controlada() -> None

Variables sugeridas:
- tarea_espera: PythonOperator
"""
