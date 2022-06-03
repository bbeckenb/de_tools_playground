from airflow.operators.python_operator import PythonOperator
from airflow import DAG
import datetime
from send_stock_data_to_S3 import send_stock_data_to_S3

with DAG(dag_id='stock_dag',
        start_date=datetime.datetime(2022,6,2),
        schedule_interval='@daily',
        catchup=False) as dag:

    task1 = PythonOperator(task_id='send_stock_data_to_S3',
                            python_callable=send_stock_data_to_S3)

task1