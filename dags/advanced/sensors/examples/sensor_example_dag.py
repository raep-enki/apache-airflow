"""
DAG Example: Sensors
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: sensors
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.python import PythonSensor
from datetime import datetime
import time

def wait_for_file():
    # Simulate waiting for a file by sleeping
    print('Waiting for file...')
    time.sleep(3)
    print('File appeared!')
    return True

def process_file():
    print('Processing file!')
    return True

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'sensor_example_dag',
    default_args=default_args,
    description='DAG demonstrating sensors',
    schedule_interval=None,
    tags=['advanced', 'example', 'sensors']
)

sensor_task = PythonSensor(
    task_id='wait_for_file',
    python_callable=wait_for_file,
    poke_interval=2,
    timeout=10,
    dag=dag
)
process_task = PythonOperator(
    task_id='process_file',
    python_callable=process_file,
    dag=dag
)

sensor_task >> process_task
