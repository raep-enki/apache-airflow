"""
Desafío: Grupos de Procesos con TaskGroup

Crea un DAG que utilice TaskGroup para organizar tareas en dos grupos: "preprocesamiento" y "procesamiento". Cada grupo debe tener al menos dos tareas y debe imprimirse el nombre del grupo y la tarea en consola. El grupo de procesamiento debe depender del de preprocesamiento.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

# TODO: Define la función tarea_en_grupo(nombre_grupo: str, nombre_tarea: str) -> None

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG

# TODO: Crea los TaskGroup "preprocesamiento" y "procesamiento" y sus tareas

# TODO: Establece las dependencias: preprocesamiento >> procesamiento

Funciones sugeridas:
- tarea_en_grupo(nombre_grupo: str, nombre_tarea: str) -> None

Variables sugeridas:
- tareas_preprocesamiento: list
- tareas_procesamiento: list
"""
