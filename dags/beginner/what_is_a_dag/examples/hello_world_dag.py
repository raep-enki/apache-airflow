"""
DAG Example: What is a DAG - Hello World
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: what_is_a_dag
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
    print('Hello, World! This is your first Airflow DAG.')
    return 'Hello, World!'

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='A minimal DAG example with Hello World',
    schedule_interval=None,
    tags=['what_is_a_dag']
)

hello_task = PythonOperator(
    task_id='say_hello',
    python_callable=hello_world,
    dag=dag
)
