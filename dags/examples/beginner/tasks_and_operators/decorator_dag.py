"""
DAG Example: Tasks and Operators with Decorators
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: tasks_and_operators
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def uppercase_decorator(func):
    def wrapper():
        result = func()
        upper = result.upper()
        print(upper)
        return upper
    return wrapper

@uppercase_decorator
def say_python():
    return 'python is awesome!'

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'decorator_dag',
    default_args=default_args,
    description='DAG with a Python decorator example',
    schedule_interval=None,
    tags=['tasks_and_operators']
)

decorator_task = PythonOperator(
    task_id='run_decorator',
    python_callable=say_python,
    dag=dag
)
