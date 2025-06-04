"""
Desafío: Saludo desde Variable de Airflow

Crea un DAG que obtenga el valor de una Variable de Airflow llamada "nombre_saludo" y lo use para imprimir un saludo personalizado en consola. Si la variable no existe, debe mostrar un saludo genérico.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime

# TODO: Define la función imprimir_saludo_variable() -> None

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG

# TODO: Crea la tarea tarea_saludo_variable usando PythonOperator

# TODO: Establece las dependencias si es necesario

Funciones sugeridas:
- imprimir_saludo_variable() -> None

Variables sugeridas:
- tarea_saludo_variable: PythonOperator
"""
