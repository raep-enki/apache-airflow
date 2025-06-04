"""
DAG Example: Disabling Catchup with Set Operations
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: disabling_catchup
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def set_operations():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    union = a | b
    intersection = a & b
    print('Union:', union)
    print('Intersection:', intersection)
    return union, intersection

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'set_operations_dag',
    default_args=default_args,
    description='DAG with catchup disabled and set operations',
    schedule_interval='@daily',
    catchup=False,
    tags=['disabling_catchup']
)

set_task = PythonOperator(
    task_id='perform_set_operations',
    python_callable=set_operations,
    dag=dag
)
