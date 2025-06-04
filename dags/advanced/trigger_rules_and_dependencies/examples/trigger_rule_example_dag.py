"""
DAG Example: Trigger Rules and Dependencies
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: trigger_rules_and_dependencies
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime

def always_succeed():
    print('This task always succeeds!')
    return True

def always_fail():
    raise Exception('This task always fails!')

def after_all():
    print('This runs after all upstream tasks finish, regardless of success.')
    return True

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'trigger_rule_example_dag',
    default_args=default_args,
    description='DAG demonstrating trigger rules',
    schedule_interval=None,
    tags=['advanced', 'example', 'trigger_rules_and_dependencies']
)

success_task = PythonOperator(
    task_id='always_succeed',
    python_callable=always_succeed,
    dag=dag
)
failure_task = PythonOperator(
    task_id='always_fail',
    python_callable=always_fail,
    dag=dag
)
after_all_task = PythonOperator(
    task_id='after_all',
    python_callable=after_all,
    trigger_rule=TriggerRule.ALL_DONE,
    dag=dag
)

[success_task, failure_task] >> after_all_task
