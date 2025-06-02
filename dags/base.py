from datetime import timedelta

from airflow import DAG
from airflow.configuration import conf
from airflow.operators.empty import EmptyOperator
from airflow.utils.types import NOTSET

import jinja2
import pendulum


tz = 'America/Mexico_City'

default_args = {
    'owner': 'Servicios Enki de México S.A.P.I. de C.V.',
    'email_on_failure': True,
    'email_on_retry': True,
    'email': [],
    'retries': 0,
    'retry_delay': timedelta(weeks=0, days=0, hours=0, minutes=0, seconds=0, microseconds=0, milliseconds=0)
}

params = {}

kwargs = {
    'dag_id': 'base',
    'description': '',
    'schedule': None,
    'schedule_interval': NOTSET,
    'timetable': None,
    'start_date': pendulum.datetime(year=2025, month=6, day=1, hour=0, minute=0, second=0, microsecond=0, tz=tz),
    'end_date': pendulum.datetime(year=2025, month=6, day=7, hour=0, minute=0, second=0, microsecond=0, tz=tz),
    'full_filepath': None,
    'template_searchpath': None,
    'template_undefined': jinja2.StrictUndefined,
    'user_defined_macros': None,
    'user_defined_filters': None,
    'default_args': default_args,
    'concurrency': None,
    'max_active_tasks': conf.getint('core', 'max_active_tasks_per_dag'),
    'max_active_runs': 1,
    # 'max_consecutive_failed_dag_runs': conf.getint('core', 'max_consecutive_failed_dag_runs_'),
    'dagrun_timeout': timedelta(weeks=0, days=0, hours=0, minutes=0, seconds=0, microseconds=0, milliseconds=0),
    'sla_miss_callback': None,
    'default_view': conf.get_mandatory_value('webserver', 'dag_default_view').lower(),
    'orientation': conf.get_mandatory_value('webserver', 'dag_orientation'),
    'catchup': conf.getboolean('scheduler', 'catchup_by_default'),
    'on_success_callback': None,
    'on_failure_callback': None,
    'doc_md': None,
    'params': params,
    'access_control': None,
    'is_paused_upon_creation': None,
    'jinja_environment_kwargs': None,
    'render_template_as_native_obj': False,
    'tags': [],
    'owner_links': None,
    'auto_register': True,
    'fail_stop': False,
    'dag_display_name': 'Base DAG'
}

with DAG(**kwargs) as dag:
    empty_task = EmptyOperator(task_id='empty_task')
