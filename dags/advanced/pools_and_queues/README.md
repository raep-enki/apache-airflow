# Pools and Queues

## Objetivo
Comprender cómo utilizar pools y queues en Apache Airflow para gestionar el acceso concurrente a recursos limitados y distribuir la carga de trabajo entre diferentes workers.

## Definición
Un pool limita el número de tareas que pueden acceder simultáneamente a un recurso compartido, como una base de datos o API. Las queues permiten asignar tareas a diferentes workers o entornos, facilitando la segmentación y priorización de cargas de trabajo.

## Ejemplo
Asignar tareas a un pool llamado "db_pool" con 2 slots disponibles:

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    'ejemplo_pools',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
)

for i in range(4):
    BashOperator(
        task_id=f'tarea_db_{i}',
        bash_command='echo "Accediendo a la base de datos"',
        pool='db_pool',
        dag=dag
    )
```

## Caso de Uso
Recomendado para controlar el acceso a recursos críticos, evitar la sobrecarga de sistemas externos y distribuir tareas entre diferentes entornos o prioridades.

## Buenas Prácticas
- Defina pools para cada recurso compartido relevante.
- Ajuste el número de slots según la capacidad del recurso.
- Utilice queues para separar cargas de trabajo por tipo o prioridad.
- Documente la asignación de pools y queues en cada DAG.
- Monitoree el uso de pools y queues para optimizar la utilización de recursos.
