"""
DAG Example: Task Retries and Retry Delay
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: task_retries_and_retry_delay
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def sometimes_fails():
    import random
    if random.random() < 0.7:
        raise Exception('Random failure!')
    print('Task succeeded!')
    return True

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
    'retries': 3,
    'retry_delay': timedelta(seconds=10),
}

dag = DAG(
    'retry_example_dag',
    default_args=default_args,
    description='DAG demonstrating retries and retry delay',
    schedule_interval=None,
    tags=['intermediate', 'example', 'task_retries_and_retry_delay']
)

retry_task = PythonOperator(
    task_id='sometimes_fails',
    python_callable=sometimes_fails,
    dag=dag
)
