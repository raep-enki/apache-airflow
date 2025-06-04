"""
Desafío: Suma de Números Pares hasta N

Crea un DAG en Airflow que reciba un número entero N y calcule la suma de todos los números pares desde 1 hasta N (incluyendo N si es par). El valor de N debe estar definido como una variable en el código. El DAG debe tener una sola tarea que realice el cálculo y muestre el resultado en consola.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# TODO: Define la función sumar_pares_hasta_n(n: int) -> int

# TODO: Define la variable numero_limite

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG

# TODO: Crea la tarea tarea_sumar_pares usando PythonOperator

# TODO: Establece las dependencias si es necesario

Funciones sugeridas:
- sumar_pares_hasta_n(n: int) -> int

Variables sugeridas:
- numero_limite: int
- resultado_suma_pares: int
- tarea_sumar_pares: PythonOperator
"""
