# Desactivación de Catchup en DAGs

## Objetivo
Evitar la ejecución retroactiva de instancias de un DAG, asegurando que solo se procese la información correspondiente a la fecha actual o futura.

## Definición
El parámetro `catchup` en un DAG de Airflow determina si el scheduler debe ejecutar instancias pasadas del DAG que no se ejecutaron en su momento. Al establecer `catchup=False`, el DAG solo ejecutará la instancia correspondiente a la fecha actual o futura, ignorando ejecuciones pendientes del pasado.

## Ejemplo
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def imprimir_fecha(**context):
    print(f"Fecha de ejecución: {context['ds']}")

dag = DAG(
    'dag_sin_catchup',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
)

mostrar_fecha = PythonOperator(
    task_id='imprimir_fecha',
    python_callable=imprimir_fecha,
    provide_context=True,
    dag=dag
)
```

## Caso de Uso
Procesos de monitoreo o notificaciones donde solo interesa la información del día actual y no tiene sentido procesar datos históricos.

## Buenas Prácticas
- Usar `catchup=False` en DAGs donde la información histórica no es relevante o puede causar sobrecarga.
- Documentar claramente en el DAG por qué se desactiva el catchup.
- Revisar la fecha de inicio (`start_date`) para evitar ejecuciones no deseadas.
