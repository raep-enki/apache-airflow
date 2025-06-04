"""
DAG Example: Task Timeouts and SLAs
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: task_timeouts_and_slas
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import time

def slow_task():
    print('Starting slow task...')
    time.sleep(5)
    print('Finished slow task!')
    return True

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'timeout_sla_dag',
    default_args=default_args,
    description='DAG demonstrating execution_timeout and SLA',
    schedule_interval=None,
    tags=['intermediate', 'example', 'task_timeouts_and_slas'],
    dag_display_name='Task Timeouts and SLAs Example'
)

timeout_task = PythonOperator(
    task_id='slow_task',
    python_callable=slow_task,
    execution_timeout=timedelta(seconds=3),
    sla=timedelta(seconds=4),
    dag=dag
)
