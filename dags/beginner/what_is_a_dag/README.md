# ¿Qué es un DAG?

## Objetivo
Entender el concepto de DAG (Directed Acyclic Graph) en Apache Airflow y su importancia en la orquestación de flujos de trabajo.

## Definición
Un DAG es una estructura de datos que representa un conjunto de tareas organizadas de forma que cada tarea depende de la anterior, sin formar ciclos. En Airflow, un DAG define el orden y la dependencia entre tareas, asegurando que se ejecuten en la secuencia correcta.

## Ejemplo
Definir un DAG simple con dos tareas secuenciales:

```python
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

dag = DAG(
    'ejemplo_que_es_un_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
)

inicio = DummyOperator(
    task_id='inicio',
    dag=dag
)

fin = DummyOperator(
    task_id='fin',
    dag=dag
)

inicio >> fin
```

## Caso de Uso
Los DAGs se utilizan para modelar procesos ETL, pipelines de datos, automatización de reportes y cualquier flujo de trabajo que requiera una secuencia de tareas dependientes.

## Buenas Prácticas
- Mantenga los DAGs simples y fáciles de entender.
- Documente el propósito y la lógica de cada DAG.
- Evite dependencias circulares entre tareas.
- Utilice nombres descriptivos para los DAGs y las tareas.
- Revise y actualice los DAGs según evolucionen los procesos de negocio.
