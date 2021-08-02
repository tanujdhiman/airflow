import pathlib
from datetime import timedelta
from textwrap import dedent

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


args = {'owner': 'airflow'}

with DAG(
    dag_id='download_file',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['download_file'],
    params={'downloadLink': 'https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_700KB.mp3'},
    ) as dag:

    download_file_command = dedent(
    """
    cd /home/airflow/output
    wget {{ params.downloadLink }} -P .
    """
    )

    t1 = BashOperator(task_id='download_file', bash_command=download_file_command)
