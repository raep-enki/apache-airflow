"""
DAG Example: Variables and Connections
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: variables_and_connections
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable, Connection
from datetime import datetime

def print_variable():
    value = Variable.get('my_variable', default_var='default_value')
    print('Variable value:', value)
    return value

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'variables_connections_dag',
    default_args=default_args,
    description='DAG demonstrating Airflow Variables and Connections',
    schedule_interval=None,
    tags=['intermediate', 'example', 'variables_and_connections']
)

variable_task = PythonOperator(
    task_id='print_variable',
    python_callable=print_variable,
    dag=dag
)
