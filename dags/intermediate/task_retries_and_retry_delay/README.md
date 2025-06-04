# Task Retries and Retry Delay

## Objetivo
Comprender cómo configurar reintentos y retrasos entre reintentos para tareas en Apache Airflow, mejorando la tolerancia a fallos y la robustez de los flujos de trabajo.

## Definición
Airflow permite definir cuántas veces una tarea debe reintentarse en caso de fallo (`retries`) y cuánto tiempo esperar entre cada intento (`retry_delay`). Esto es útil para manejar errores transitorios, como caídas temporales de servicios externos.

## Ejemplo
Configurar una tarea para que se reintente hasta 3 veces, esperando 5 minutos entre cada intento:

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

dag = DAG(
    'ejemplo_reintentos',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
)

tarea = BashOperator(
    task_id='tarea_inestable',
    bash_command='exit 1',
    retries=3,
    retry_delay=timedelta(minutes=5),
    dag=dag
)
```

## Caso de Uso
Recomendado para tareas que dependen de servicios externos susceptibles a fallos intermitentes, como APIs, bases de datos o sistemas de archivos remotos.

## Buenas Prácticas
- Ajuste el número de reintentos y el retraso según la criticidad y la naturaleza del fallo esperado.
- Evite reintentos excesivos que puedan saturar recursos o generar efectos secundarios.
- Monitoree los logs para identificar patrones de fallos recurrentes.
- Combine los reintentos con alertas para intervención manual si es necesario.
- Documente la lógica de reintentos en el DAG para facilitar el mantenimiento.
