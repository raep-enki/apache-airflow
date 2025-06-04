# Estructura Básica de un DAG

## Objetivo
Comprender cómo se define y organiza la estructura fundamental de un DAG en Apache Airflow para modelar flujos de trabajo claros y eficientes.

## Definición
Un DAG (Directed Acyclic Graph) es la base de cualquier pipeline en Airflow. Representa un conjunto de tareas (nodos) y sus dependencias (aristas), asegurando que el flujo de ejecución no tenga ciclos. La estructura básica de un DAG incluye la declaración del objeto `DAG`, la definición de tareas y el establecimiento de dependencias entre ellas.

## Ejemplo
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def imprimir_mensaje():
    print("¡Hola desde mi primer DAG!")

dag = DAG(
    'mi_dag_basico',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None
)

saludo = PythonOperator(
    task_id='imprimir_mensaje',
    python_callable=imprimir_mensaje,
    dag=dag
)
```

## Caso de Uso
Automatización de un proceso de ETL simple donde primero se extraen datos, luego se transforman y finalmente se cargan en un destino. Cada paso es una tarea y la estructura básica del DAG define el orden de ejecución.

## Buenas Prácticas
- Utilizar nombres descriptivos para el DAG y las tareas.
- Mantener la estructura del DAG simple y fácil de leer.
- Definir dependencias de manera explícita usando `>>` o `set_downstream`.
- Documentar el propósito del DAG y cada tarea con comentarios o docstrings.
- Evitar lógica compleja directamente en la definición del DAG; delegar la lógica a funciones externas.
