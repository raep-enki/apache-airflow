# Trigger Rules and Dependencies

## Objetivo
Aprender a controlar la ejecución de tareas en Apache Airflow mediante reglas de activación (trigger rules) y dependencias personalizadas, permitiendo flujos de trabajo flexibles y adaptables.

## Definición
Las trigger rules determinan bajo qué condiciones se ejecuta una tarea, considerando el estado de las tareas predecesoras. Airflow ofrece reglas como `all_success`, `one_failed`, `all_done`, entre otras, para modelar dependencias complejas.

## Ejemplo
Ejecutar una tarea solo si al menos una tarea previa falla:

```python
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime

dag = DAG(
    'ejemplo_trigger_rules',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
)

t1 = DummyOperator(task_id='tarea_1', dag=dag)
t2 = DummyOperator(task_id='tarea_2', dag=dag)
alerta = DummyOperator(
    task_id='alerta',
    trigger_rule=TriggerRule.ONE_FAILED,
    dag=dag
)

[t1, t2] >> alerta
```

## Caso de Uso
Útil para flujos de trabajo donde se requiere ejecutar tareas de compensación, alertas o rutas alternativas según el resultado de tareas previas.

## Buenas Prácticas
- Seleccione la trigger rule adecuada para cada caso de uso.
- Documente las dependencias y reglas de activación en el DAG.
- Pruebe los diferentes escenarios de ejecución para validar el comportamiento esperado.
- Evite dependencias circulares o reglas ambiguas.
- Revise periódicamente la lógica de dependencias para adaptarse a cambios en el flujo de trabajo.
