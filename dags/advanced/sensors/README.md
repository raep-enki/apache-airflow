# Sensors

## Objetivo
Aprender a utilizar sensores en Apache Airflow para esperar eventos o condiciones externas antes de continuar con la ejecución de un flujo de trabajo.

## Definición
Un sensor es un tipo especial de operador que pausa la ejecución de un DAG hasta que se cumple una condición, como la llegada de un archivo, la disponibilidad de una tabla o la respuesta de un servicio externo.

## Ejemplo
Esperar la existencia de un archivo antes de ejecutar una tarea:

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

dag = DAG(
    'ejemplo_sensor',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
)

esperar_archivo = FileSensor(
    task_id='esperar_archivo',
    filepath='/ruta/al/archivo.txt',
    poke_interval=60,
    timeout=600,
    dag=dag
)

procesar = BashOperator(
    task_id='procesar_archivo',
    bash_command='cat /ruta/al/archivo.txt',
    dag=dag
)

esperar_archivo >> procesar
```

## Caso de Uso
Común en integraciones con sistemas externos, donde es necesario esperar la llegada de datos, la finalización de procesos o la disponibilidad de recursos antes de continuar.

## Buenas Prácticas
- Defina timeouts razonables para evitar bloqueos prolongados.
- Utilice sensores de tipo "poke" para condiciones simples y "reschedule" para esperas largas.
- Monitoree el uso de sensores para optimizar el rendimiento del scheduler.
- Documente claramente la condición que activa el sensor.
- Evite el uso excesivo de sensores en paralelo para no saturar el entorno.
