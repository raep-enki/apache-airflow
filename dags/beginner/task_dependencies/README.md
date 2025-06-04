# Dependencias entre Tareas en DAGs

## Objetivo
Entender cómo definir y gestionar el orden de ejecución entre tareas dentro de un DAG, asegurando que cada paso del flujo de trabajo se realice en el momento adecuado.

## Definición
Las dependencias entre tareas en Airflow determinan la secuencia en la que se ejecutan las tareas dentro de un DAG. Se establecen utilizando operadores como `>>` y `<<`, o métodos como `set_downstream` y `set_upstream`. Estas dependencias permiten modelar flujos lineales, ramificados o complejos, garantizando que una tarea no inicie hasta que sus predecesoras hayan finalizado correctamente.

## Ejemplo
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extraer():
    print("Extrayendo datos...")

def transformar():
    print("Transformando datos...")

def cargar():
    print("Cargando datos...")

dag = DAG(
    'dag_dependencias',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None
)

extraer_tarea = PythonOperator(task_id='extraer', python_callable=extraer, dag=dag)
transformar_tarea = PythonOperator(task_id='transformar', python_callable=transformar, dag=dag)
cargar_tarea = PythonOperator(task_id='cargar', python_callable=cargar, dag=dag)

extraer_tarea >> transformar_tarea >> cargar_tarea
```

## Caso de Uso
Un pipeline ETL donde es fundamental que la transformación de datos ocurra solo después de la extracción, y la carga solo después de la transformación, asegurando la integridad del proceso.

## Buenas Prácticas
- Definir dependencias de manera explícita y legible.
- Evitar dependencias circulares, ya que los DAGs deben ser acíclicos.
- Documentar el propósito de cada dependencia cuando el flujo sea complejo.
- Utilizar nombres de tareas descriptivos para facilitar el seguimiento del flujo.
- Revisar visualmente el DAG en la interfaz de Airflow para validar la secuencia de tareas.
