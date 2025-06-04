"""
DAG Example: Basic DAG Structure with Fibonacci
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: basic_dag_structure
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    print('Fibonacci sequence:', sequence)
    return sequence

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'fibonacci_dag',
    default_args=default_args,
    description='A simple DAG structure using Fibonacci sequence',
    schedule_interval=None,
    tags=['basic_dag_structure']
)

fibonacci_task = PythonOperator(
    task_id='calculate_fibonacci',
    python_callable=fibonacci,
    op_args=[10],
    dag=dag
)
