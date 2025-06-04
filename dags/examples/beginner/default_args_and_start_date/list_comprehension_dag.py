"""
DAG Example: Default Args and Start Date with List Comprehension
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: default_args_and_start_date
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def squares():
    result = [x**2 for x in range(10)]
    print('Squares:', result)
    return result

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'list_comprehension_dag',
    default_args=default_args,
    description='DAG with default args and list comprehension',
    schedule_interval='@daily',
    tags=['default_args_and_start_date']
)

squares_task = PythonOperator(
    task_id='calculate_squares',
    python_callable=squares,
    dag=dag
)
