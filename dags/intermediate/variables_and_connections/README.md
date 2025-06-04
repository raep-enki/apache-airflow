# Variables and Connections

## Objetivo
Aprender a gestionar variables y conexiones en Apache Airflow para almacenar configuraciones y credenciales de manera segura y centralizada.

## Definición
Las variables permiten almacenar valores dinámicos o de configuración accesibles desde cualquier DAG. Las conexiones gestionan credenciales y parámetros de acceso a sistemas externos, facilitando la integración segura y reutilizable.

## Ejemplo
Acceder a una variable y una conexión desde una tarea Python:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable, Connection
from datetime import datetime

def usar_variables_conexiones(**kwargs):
    valor = Variable.get('mi_variable', default_var='valor_por_defecto')
    # Las conexiones se acceden normalmente a través de hooks
    print(f"Valor de la variable: {valor}")


dag = DAG(
    'ejemplo_variables_conexiones',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
)

PythonOperator(
    task_id='mostrar_variable',
    python_callable=usar_variables_conexiones,
    dag=dag
)
```

## Caso de Uso
Recomendado para almacenar rutas de archivos, parámetros de conexión, claves API o cualquier configuración que pueda cambiar entre entornos.

## Buenas Prácticas
- No almacene credenciales sensibles directamente en el código fuente.
- Utilice el Airflow UI o CLI para gestionar variables y conexiones.
- Documente el propósito de cada variable y conexión.
- Implemente controles de acceso para proteger información sensible.
- Revise y actualice periódicamente las variables y conexiones según las necesidades del proyecto.
