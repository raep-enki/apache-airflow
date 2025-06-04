"""
DAG Example: Branching with PythonOperator
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: branching
"""
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime

def choose_branch():
    import random
    return 'branch_a' if random.choice([True, False]) else 'branch_b'

def branch_a():
    print('Branch A executed')
    return 'A'

def branch_b():
    print('Branch B executed')
    return 'B'

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'branching_python_operator_dag',
    default_args=default_args,
    description='DAG demonstrating branching with PythonOperator',
    schedule_interval=None,
    tags=['intermediate', 'example', 'branching']
)

branch_task = BranchPythonOperator(
    task_id='branch_task',
    python_callable=choose_branch,
    dag=dag
)
branch_a_task = PythonOperator(
    task_id='branch_a',
    python_callable=branch_a,
    dag=dag
)
branch_b_task = PythonOperator(
    task_id='branch_b',
    python_callable=branch_b,
    dag=dag
)

branch_task >> [branch_a_task, branch_b_task]
