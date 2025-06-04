"""
DAG Example: Scheduling with Cron
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: scheduling_with_cron
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_time():
    print('This DAG runs every day at 7:30 AM!')
    return True

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'cron_schedule_dag',
    default_args=default_args,
    description='DAG scheduled with a cron expression',
    schedule_interval='30 7 * * *',
    tags=['intermediate', 'example', 'scheduling_with_cron']
)

cron_task = PythonOperator(
    task_id='print_time',
    python_callable=print_time,
    dag=dag
)
