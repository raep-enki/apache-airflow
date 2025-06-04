"""
DAG Example: Task Groups and Complex Workflows
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: task_groups_and_complex_workflows
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

def print_task(task):
    print(f"Task: {task}")
    return task

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'task_group_example_dag',
    default_args=default_args,
    description='DAG demonstrating TaskGroup',
    schedule_interval=None,
    tags=['task_groups_and_complex_workflows']
)

with TaskGroup('group1', dag=dag) as group1:
    for i in range(2):
        PythonOperator(
            task_id=f'group1_task_{i}',
            python_callable=print_task,
            op_args=[f'group1_task_{i}'],
            dag=dag
        )
with TaskGroup('group2', dag=dag) as group2:
    for i in range(2):
        PythonOperator(
            task_id=f'group2_task_{i}',
            python_callable=print_task,
            op_args=[f'group2_task_{i}'],
            dag=dag
        )

group1 >> group2
