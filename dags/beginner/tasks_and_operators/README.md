# Tasks and Operators

## Objetivo
Comprender la diferencia entre tareas y operadores en Apache Airflow, y aprender a utilizar los distintos tipos de operadores para definir acciones dentro de un DAG.

## Definición
En Airflow, una tarea es una instancia de un operador. Los operadores son clases que definen la naturaleza de la acción a ejecutar, como ejecutar un comando Bash, una función Python, o transferir datos. Los tipos más comunes son BashOperator, PythonOperator, DummyOperator, entre otros.

## Ejemplo
Definir un DAG con tres tareas usando diferentes operadores:

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

dag = DAG(
    'ejemplo_tareas_operadores',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
)

tarea_bash = BashOperator(
    task_id='imprimir_fecha',
    bash_command='date',
    dag=dag
)

tarea_python = PythonOperator(
    task_id='saludar',
    python_callable=lambda: print('¡Hola, Airflow!'),
    dag=dag
)

tarea_dummy = DummyOperator(
    task_id='fin',
    dag=dag
)

tarea_bash >> tarea_python >> tarea_dummy
```

## Caso de Uso
Ideal para orquestar flujos de trabajo que requieren ejecutar scripts, procesar datos, o simplemente marcar el inicio o fin de un proceso.

## Buenas Prácticas
- Seleccione el operador adecuado según la acción a realizar.
- Mantenga las tareas atómicas y bien definidas.
- Documente el propósito de cada tarea y operador.
- Evite lógica compleja dentro de los operadores; prefiera funciones externas.
- Pruebe cada tarea de forma individual antes de integrarla al DAG.
