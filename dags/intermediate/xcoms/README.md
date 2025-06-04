# XComs

## Objetivo
Comprender cómo intercambiar datos entre tareas en Apache Airflow utilizando XComs, permitiendo flujos de trabajo más dinámicos y colaborativos.

## Definición
XCom (Cross-Communication) es un mecanismo de Airflow para compartir información entre tareas de un mismo DAG. Las tareas pueden enviar (push) y recibir (pull) datos, facilitando la coordinación y el paso de resultados intermedios.

## Ejemplo
Enviar y recibir un valor entre dos tareas:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def enviar_valor(**kwargs):
    kwargs['ti'].xcom_push(key='resultado', value=42)

def recibir_valor(**kwargs):
    valor = kwargs['ti'].xcom_pull(key='resultado', task_ids='enviar')
    print(f"Valor recibido: {valor}")

dag = DAG(
    'ejemplo_xcom',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
)

PythonOperator(
    task_id='enviar',
    python_callable=enviar_valor,
    provide_context=True,
    dag=dag
) >> PythonOperator(
    task_id='recibir',
    python_callable=recibir_valor,
    provide_context=True,
    dag=dag
)
```

## Caso de Uso
Útil para pasar resultados de procesamiento, rutas de archivos generadas dinámicamente o cualquier información que deba ser utilizada por tareas posteriores.

## Buenas Prácticas
- Limite el tamaño de los datos transmitidos por XComs para evitar sobrecargar la base de datos de Airflow.
- Utilice claves descriptivas para identificar los valores almacenados.
- Documente el flujo de datos entre tareas.
- Prefiera XComs para datos pequeños y temporales; para grandes volúmenes, utilice almacenamiento externo.
- Monitoree el uso de XComs para evitar acumulación innecesaria de registros.
