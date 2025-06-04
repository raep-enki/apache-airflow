"""
Desafío: Suma de Números Naturales

Crea un DAG en Airflow que reciba un número entero N y calcule la suma de los primeros N números naturales. El valor de N debe estar definido como una variable en el código. El DAG debe tener una sola tarea que realice el cálculo y muestre el resultado en consola.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# TODO: Define la función calcular_suma_naturales(n: int) -> int

# TODO: Define la variable cantidad_numeros

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG

# TODO: Crea la tarea tarea_suma_naturales usando PythonOperator

# TODO: Establece las dependencias si es necesario

Funciones sugeridas:
- calcular_suma_naturales(n: int) -> int

Variables sugeridas:
- cantidad_numeros: int
- resultado_suma: int
- tarea_suma_naturales: PythonOperator
"""
