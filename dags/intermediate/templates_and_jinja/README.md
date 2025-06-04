# Templates and Jinja

## Objetivo
Entender cómo utilizar plantillas y el motor Jinja en Apache Airflow para parametrizar tareas y hacer flujos de trabajo más dinámicos y reutilizables.

## Definición
Airflow permite el uso de plantillas Jinja en parámetros de tareas, facilitando la inserción dinámica de variables como fechas, rutas o valores calculados. Esto incrementa la flexibilidad y adaptabilidad de los DAGs.

## Ejemplo
Uso de una plantilla Jinja para incluir la fecha de ejecución en un comando Bash:

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    'ejemplo_jinja',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
)

tarea = BashOperator(
    task_id='imprimir_fecha',
    bash_command='echo "La fecha de ejecución es: {{ ds }}"',
    dag=dag
)
```

## Caso de Uso
Ideal para generar rutas de archivos dinámicas, nombres de tablas, o personalizar mensajes y comandos según el contexto de ejecución.

## Buenas Prácticas
- Valide las variables disponibles en la documentación oficial de Airflow.
- Evite lógica compleja dentro de las plantillas para mantener la legibilidad.
- Documente el uso de variables y plantillas en el DAG.
- Pruebe los DAGs con diferentes fechas y parámetros para asegurar el correcto funcionamiento de las plantillas.
- Utilice plantillas para reducir la duplicidad de código y mejorar la mantenibilidad.
