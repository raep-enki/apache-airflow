"""
Desafío: Condiciones Finales con Trigger Rules

Crea un DAG con al menos tres tareas iniciales, donde una de las tareas finales debe ejecutarse solo si al menos una de las tareas iniciales falla (TriggerRule.ONE_FAILED) y otra solo si todas tienen éxito (TriggerRule.ALL_SUCCESS).

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime

# TODO: Define la función tarea_exito() -> None
# TODO: Define la función tarea_fallo() -> None
# TODO: Define la función tarea_final_uno_failed() -> None
# TODO: Define la función tarea_final_all_success() -> None

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG

# TODO: Crea las tareas iniciales y las tareas finales con los trigger rules adecuados

# TODO: Establece las dependencias: tareas_iniciales >> [tarea_final_fallo, tarea_final_exito]

Funciones sugeridas:
- tarea_exito() -> None
- tarea_fallo() -> None
- tarea_final_uno_failed() -> None
- tarea_final_all_success() -> None

Variables sugeridas:
- tareas_iniciales: list
- tarea_final_fallo: PythonOperator
- tarea_final_exito: PythonOperator
"""
