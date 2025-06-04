"""
DAG Example: Templates and Jinja
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: templates_and_jinja
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_context(ds, **kwargs):
    print(f"Today's execution date is: {ds}")
    return ds

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'jinja_template_dag',
    default_args=default_args,
    description='DAG demonstrating Jinja templating',
    schedule_interval=None,
    tags=['intermediate', 'example', 'templates_and_jinja'],
    dag_display_name='Templates and Jinja Example'
)

template_task = PythonOperator(
    task_id='print_context',
    python_callable=print_context,
    op_args=['{{ ds }}'],
    provide_context=True,
    dag=dag
)
