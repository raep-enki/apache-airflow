# Dynamic DAG Generation

## Objetivo
Aprender a generar DAGs de forma dinámica en Apache Airflow, permitiendo la creación automática de flujos de trabajo a partir de configuraciones externas o patrones repetitivos.

## Definición
La generación dinámica de DAGs consiste en crear múltiples DAGs o tareas a partir de listas, archivos de configuración o bases de datos, evitando la duplicación de código y facilitando la escalabilidad y el mantenimiento.

## Ejemplo
Crear varios DAGs a partir de una lista de clientes:

```python
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

clientes = ['cliente_a', 'cliente_b', 'cliente_c']

def crear_dag(cliente):
    with DAG(
        f'proceso_{cliente}',
        start_date=datetime(2023, 1, 1),
        schedule_interval='@daily',
        catchup=False
    ) as dag:
        DummyOperator(task_id='inicio')
    return dag

for cliente in clientes:
    globals()[f'dag_{cliente}'] = crear_dag(cliente)
```

## Caso de Uso
Ideal para escenarios multi-tenant, procesamiento de múltiples fuentes de datos o automatización de flujos de trabajo repetitivos con parámetros variables.

## Buenas Prácticas
- Mantenga la lógica de generación dinámica clara y documentada.
- Valide las configuraciones externas antes de crear los DAGs.
- Evite la creación excesiva de DAGs que puedan saturar el scheduler.
- Utilice nombres descriptivos y únicos para cada DAG generado.
- Pruebe la generación dinámica en entornos controlados antes de implementarla en producción.
