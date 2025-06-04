# Scheduling with Cron

## Objetivo
Aprender a programar la ejecución de DAGs en Apache Airflow utilizando expresiones cron para definir horarios personalizados y recurrentes.

## Definición
El scheduling con cron en Airflow permite especificar cuándo y con qué frecuencia se ejecuta un DAG, utilizando expresiones cron estándar. Esto proporciona flexibilidad para programar tareas en intervalos complejos, como días específicos de la semana, horas concretas o patrones personalizados.

## Ejemplo
Para ejecutar un DAG cada lunes y miércoles a las 7:30 AM:

```python
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

dag = DAG(
    'ejemplo_cron',
    start_date=datetime(2023, 1, 1),
    schedule_interval='30 7 * * 1,3',  # Lunes y miércoles a las 7:30
    catchup=False
)

tarea = DummyOperator(
    task_id='inicio',
    dag=dag
)
```

## Caso de Uso
Ideal para procesos que deben ejecutarse en horarios específicos, como cierres contables mensuales, reportes semanales o tareas nocturnas de mantenimiento.

## Buenas Prácticas
- Utilice la notación cron estándar y valide las expresiones antes de usarlas.
- Documente claramente el propósito y la frecuencia del DAG.
- Considere el uso de `catchup=False` para evitar ejecuciones retroactivas no deseadas.
- Sincronice los horarios de ejecución con las dependencias externas para evitar conflictos.
- Revise periódicamente los horarios para ajustarlos a cambios en los requerimientos del negocio.
