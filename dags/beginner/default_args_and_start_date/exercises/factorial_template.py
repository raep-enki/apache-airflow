"""
Desafío: Cálculo de Factorial con Parámetros por Defecto

Crea un DAG que calcule el factorial de un número N, donde N es una variable definida en el código. Configura los argumentos por defecto (default_args) para que el DAG tenga un propietario, una fecha de inicio y dos reintentos con un retraso de 5 segundos. El DAG debe tener una sola tarea que realice el cálculo y muestre el resultado en consola.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# TODO: Define la función calcular_factorial(n: int) -> int

# TODO: Define la variable numero_factorial

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG

# TODO: Crea la tarea tarea_factorial usando PythonOperator

# TODO: Establece las dependencias si es necesario

Funciones sugeridas:
- calcular_factorial(n: int) -> int

Variables sugeridas:
- numero_factorial: int
- resultado_factorial: int
- tarea_factorial: PythonOperator
"""
