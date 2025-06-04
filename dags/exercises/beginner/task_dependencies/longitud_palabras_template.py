"""
Desafío: Calcular Longitud de Palabras con Dependencias de Tareas

Crea un DAG que reciba una frase, la divida en palabras, calcule la longitud de cada palabra y luego sume todas las longitudes. Cada paso debe ser una tarea diferente y las dependencias deben estar correctamente definidas.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# TODO: Define la función dividir_frase(frase: str) -> list
# TODO: Define la función calcular_longitudes(palabras: list) -> list
# TODO: Define la función sumar_longitudes(longitudes: list) -> int

# TODO: Define la variable frase_original

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG

# TODO: Crea las tareas tarea_dividir, tarea_longitudes, tarea_sumar usando PythonOperator

# TODO: Establece las dependencias: dividir -> longitudes -> sumar

Funciones sugeridas:
- dividir_frase(frase: str) -> list
- calcular_longitudes(palabras: list) -> list
- sumar_longitudes(longitudes: list) -> int

Variables sugeridas:
- frase_original: str
- tarea_dividir: PythonOperator
- tarea_longitudes: PythonOperator
- tarea_sumar: PythonOperator
"""
