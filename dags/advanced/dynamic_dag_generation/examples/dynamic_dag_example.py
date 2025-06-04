"""
DAG Example: Dynamic DAG Generation
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: dynamic_dag_generation
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_number(n):
    print(f"Number: {n}")
    return n

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'dynamic_dag_example',
    default_args=default_args,
    description='DAG generated dynamically with a loop',
    schedule_interval=None,
    tags=['advanced', 'example', 'dynamic_dag_generation'],
    dag_display_name='Dynamic DAG Generation Example'
)

for i in range(5):
    PythonOperator(
        task_id=f'print_number_{i}',
        python_callable=print_number,
        op_args=[i],
        dag=dag
    )
