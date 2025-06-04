# Concurrency and Parallelism

## Objetivo
Comprender cómo Apache Airflow gestiona la concurrencia y el paralelismo para optimizar la ejecución simultánea de tareas y DAGs, maximizando el uso de recursos disponibles.

## Definición
La concurrencia se refiere al número de tareas que pueden ejecutarse al mismo tiempo en todo el entorno de Airflow. El paralelismo define cuántas tareas pueden ejecutarse simultáneamente por DAG o por worker. Estos parámetros se configuran a nivel global, de DAG y de tarea para controlar la carga y evitar la saturación de recursos.

## Ejemplo
Configurar un DAG para permitir un máximo de 3 tareas en paralelo:

```python
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

dag = DAG(
    'ejemplo_concurrencia',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    max_active_tasks=3,
    catchup=False
)

for i in range(5):
    DummyOperator(
        task_id=f'tarea_{i}',
        dag=dag
    )
```

## Caso de Uso
Esencial en entornos donde múltiples procesos deben ejecutarse simultáneamente, como cargas masivas de datos, procesamiento distribuido o integración de sistemas heterogéneos.

## Buenas Prácticas
- Ajuste los parámetros de concurrencia según la capacidad de la infraestructura.
- Monitoree el uso de recursos y ajuste los límites para evitar cuellos de botella.
- Utilice pools para controlar el acceso a recursos compartidos.
- Documente la configuración de concurrencia y paralelismo en cada DAG.
- Revise periódicamente los valores configurados para adaptarse a cambios en la demanda.
