from airflow import DAG
from airflow.operators import *
from airflow.operators.sensors import *
from datetime import timedelta, datetime
from pandas import *
from sqlalchemy import *
import airflow.utils
import glob, os
from rpy2 import robjects
import filecmp
import shutil
import logging

default_args = {
	    'owner': 'jyen',
        'depends_on_past': False,
        'start_date': datetime.today(),
        'email': ['jyen@makomedical.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight' : 10,
        # 'schedule_interval': timedelta(1),
        # 'end_date': datetime(2016, 1, 1),
        }
dag = DAG('qc_process', default_args=default_args,schedule_interval=timedelta(minutes=30))

COMMAND = """python /home/jyen/airflow/qc_process-dev.py """
findnewruns_newdb = BashOperator(task_id='qc_process',bash_command =COMMAND, dag=dag)