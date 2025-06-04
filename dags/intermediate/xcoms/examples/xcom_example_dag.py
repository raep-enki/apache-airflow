"""
DAG Example: XComs
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: xcoms
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def push_xcom(**context):
    context['ti'].xcom_push(key='sample_key', value='pushed_value')
    print('Pushed XCom!')

def pull_xcom(**context):
    value = context['ti'].xcom_pull(key='sample_key', task_ids='push_xcom')
    print('Pulled XCom value:', value)
    return value

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'xcom_example_dag',
    default_args=default_args,
    description='DAG demonstrating XComs',
    schedule_interval=None,
    tags=['intermediate', 'example', 'xcoms'],
    dag_display_name='XComs Example'
)

push_task = PythonOperator(
    task_id='push_xcom',
    python_callable=push_xcom,
    provide_context=True,
    dag=dag
)
pull_task = PythonOperator(
    task_id='pull_xcom',
    python_callable=pull_xcom,
    provide_context=True,
    dag=dag
)

push_task >> pull_task
