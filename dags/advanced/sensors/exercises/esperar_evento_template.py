"""
Desafío: Esperar un Evento con Sensor Personalizado

Crea un DAG que utilice un sensor personalizado para esperar un evento simulado (por ejemplo, la aparición de un valor en una variable o archivo). Cuando el evento ocurra, ejecuta una tarea que procese el evento e imprima un mensaje en consola.

Plantilla sugerida:

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.base import BaseSensorOperator
from datetime import datetime

# TODO: Define la clase EventoSensor heredando de BaseSensorOperator
# TODO: Implementa el método poke para simular la espera del evento
# TODO: Define la función procesar_evento() -> None

# TODO: Configura los argumentos por defecto (default_args)

# TODO: Crea el objeto DAG

# TODO: Crea la tarea sensor_evento usando EventoSensor
# TODO: Crea la tarea tarea_procesar_evento usando PythonOperator

# TODO: Establece las dependencias: sensor_evento >> tarea_procesar_evento

Funciones sugeridas:
- procesar_evento() -> None

Variables sugeridas:
- tarea_sensor_evento: EventoSensor
- tarea_procesar_evento: PythonOperator
"""
