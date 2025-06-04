"""
DAG Example: Task Dependencies with String Formatting
Owner: Servicios Enki de México S.A.P.I. de C.V.
Tag: task_dependencies
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def split_sentence(sentence):
    words = sentence.split()
    print('Words:', words)
    return words

def capitalize_words(words):
    capitalized = [w.capitalize() for w in words]
    print('Capitalized:', capitalized)
    return capitalized

def join_words(words):
    result = ' '.join(words)
    print('Joined:', result)
    return result

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'string_formatting_dag',
    default_args=default_args,
    description='DAG showing task dependencies and string formatting',
    schedule_interval=None,
    tags=['beginner', 'example', 'task_dependencies']
)

split_task = PythonOperator(
    task_id='split_sentence',
    python_callable=split_sentence,
    op_args=['airflow is awesome'],
    dag=dag
)

capitalize_task = PythonOperator(
    task_id='capitalize_words',
    python_callable=capitalize_words,
    dag=dag
)

join_task = PythonOperator(
    task_id='join_words',
    python_callable=join_words,
    dag=dag
)

split_task >> capitalize_task >> join_task
