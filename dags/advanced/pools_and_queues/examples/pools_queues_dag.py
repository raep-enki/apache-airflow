"""
DAG Example: Pools and Queues
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: pools_and_queues
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time

def pool_task(task_number):
    print(f"Task {task_number} running in pool!")
    time.sleep(2)
    return task_number

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'pools_queues_dag',
    default_args=default_args,
    description='DAG demonstrating pools and queues',
    schedule_interval=None,
    tags=['advanced', 'example', 'pools_and_queues'],
    dag_display_name='Pools and Queues Example'
)

for i in range(3):
    PythonOperator(
        task_id=f'pool_task_{i}',
        python_callable=pool_task,
        op_args=[i],
        pool='default_pool',
        queue='default',
        dag=dag
    )
