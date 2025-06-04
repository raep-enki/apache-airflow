"""
Desafío: Saludo Programado con Cron

Crea un DAG que imprima un saludo personalizado en consola todos los días a las 6:30 AM usando una expresión cron. El saludo debe estar definido como variable en el código.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# TODO: Define la función imprimir_saludo(saludo: str) -> None

# TODO: Define la variable saludo_personalizado

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG con schedule_interval usando cron

# TODO: Crea la tarea tarea_saludo_cron usando PythonOperator

# TODO: Establece las dependencias si es necesario

Funciones sugeridas:
- imprimir_saludo(saludo: str) -> None

Variables sugeridas:
- saludo_personalizado: str
- tarea_saludo_cron: PythonOperator
"""
