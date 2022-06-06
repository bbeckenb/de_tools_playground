from airflow.operators.python_operator import PythonOperator
from airflow import DAG
import datetime
from send_stock_data_to_S3 import send_stock_data_to_S3
from get_query_res_from_s3 import get_file_send_email

with DAG(dag_id='stock_dag',
        start_date=datetime.datetime(2022,6,2),
        schedule_interval='@daily',
        catchup=False) as dag:

    task1 = PythonOperator(task_id='send_stock_data_to_S3',
                            python_callable=send_stock_data_to_S3)
    task2 = PythonOperator(task_id='send_report_via_email',
                            python_callable=get_file_send_email)
task1 >> task2