# Argumentos por Defecto y Fecha de Inicio en DAGs

## Objetivo
Aprender a configurar parámetros globales para todas las tareas de un DAG, como el propietario, la fecha de inicio y las políticas de reintentos, facilitando la gestión y el mantenimiento de los flujos de trabajo.

## Definición
Los `default_args` son un diccionario de parámetros que se aplican por defecto a todas las tareas de un DAG, permitiendo definir propiedades como el propietario (`owner`), la fecha de inicio (`start_date`), el número de reintentos (`retries`) y el tiempo de espera entre reintentos (`retry_delay`). La correcta configuración de estos parámetros es esencial para el control y la robustez de la ejecución.

## Ejemplo
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def tarea_demo():
    print("Tarea ejecutada")

default_args = {
    'owner': 'data_team',
    'start_date': datetime(2024, 1, 1),
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'dag_con_default_args',
    default_args=default_args,
    schedule_interval=None
)

operador = PythonOperator(
    task_id='tarea_demo',
    python_callable=tarea_demo,
    dag=dag
)
```

## Caso de Uso
Procesos de integración de datos donde es importante controlar los reintentos ante fallos temporales y definir claramente cuándo debe comenzar la ejecución del pipeline.

## Buenas Prácticas
- Definir `default_args` en un solo lugar y reutilizarlos en todos los DAGs similares.
- Usar fechas de inicio realistas y no en el pasado remoto para evitar ejecuciones innecesarias.
- Ajustar el número de reintentos y el tiempo de espera según la criticidad del proceso.
- Documentar el propósito de cada parámetro en los comentarios del código.
