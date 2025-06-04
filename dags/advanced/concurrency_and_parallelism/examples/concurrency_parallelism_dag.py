"""
DAG Example: Concurrency and Parallelism
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: concurrency_and_parallelism
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time

def sleep_task(task_number):
    print(f"Task {task_number} sleeping...")
    time.sleep(5)
    print(f"Task {task_number} done!")
    return task_number

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'concurrency_parallelism_dag',
    default_args=default_args,
    description='DAG demonstrating concurrency and parallelism',
    schedule_interval=None,
    max_active_tasks=2,
    concurrency=2,
    tags=['concurrency_and_parallelism']
)

for i in range(4):
    PythonOperator(
        task_id=f'sleep_task_{i}',
        python_callable=sleep_task,
        op_args=[i],
        dag=dag
    )
