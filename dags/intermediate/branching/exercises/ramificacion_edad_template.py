"""
Desafío: Ramas según Edad con BranchPythonOperator

Crea un DAG que, según el valor de una variable edad, decida si ejecutar una tarea para "mayores de edad" o una para "menores de edad" usando BranchPythonOperator. Cada rama debe imprimir un mensaje distinto en consola.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime

# TODO: Define la función decidir_rama(edad: int) -> str
# TODO: Define la función tarea_mayor_edad() -> None
# TODO: Define la función tarea_menor_edad() -> None

# TODO: Define la variable edad

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG

# TODO: Crea las tareas branch, mayor_edad, menor_edad

# TODO: Establece las dependencias: branch >> [mayor_edad, menor_edad]

Funciones sugeridas:
- decidir_rama(edad: int) -> str
- tarea_mayor_edad() -> None
- tarea_menor_edad() -> None

Variables sugeridas:
- edad: int
- tarea_branch: BranchPythonOperator
- tarea_mayor_edad: PythonOperator
- tarea_menor_edad: PythonOperator
"""
