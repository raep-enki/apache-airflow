# Task Timeouts and SLAs

## Objetivo
Aprender a establecer límites de tiempo y acuerdos de nivel de servicio (SLAs) para tareas en Apache Airflow, garantizando la ejecución oportuna y la detección de cuellos de botella.

## Definición
Un timeout define el tiempo máximo permitido para la ejecución de una tarea. Un SLA (Service Level Agreement) especifica el tiempo máximo en el que una tarea o DAG debe completarse. Airflow puede notificar si se exceden estos límites, facilitando la supervisión y mejora de procesos.

## Ejemplo
Configurar una tarea con un timeout de 10 minutos y un SLA de 15 minutos:

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

dag = DAG(
    'ejemplo_timeouts_sla',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
)

tarea = BashOperator(
    task_id='tarea_lenta',
    bash_command='sleep 600',
    execution_timeout=timedelta(minutes=10),
    sla=timedelta(minutes=15),
    dag=dag
)
```

## Caso de Uso
Útil para procesos críticos donde el tiempo de respuesta es fundamental, como cargas de datos nocturnas, generación de reportes o integraciones con ventanas de tiempo limitadas.

## Buenas Prácticas
- Defina timeouts y SLAs realistas según la naturaleza de la tarea.
- Utilice alertas para notificar incumplimientos de SLAs.
- Analice las causas de los timeouts para optimizar el rendimiento.
- Documente los límites establecidos y su justificación.
- Revise periódicamente los valores configurados para adaptarse a cambios en el entorno.
