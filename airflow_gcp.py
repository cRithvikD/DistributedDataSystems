from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.providers.mongo.hooks.mongo import MongoHook
from datetime import datetime, timedelta
import json

default_args = {
    'owner': 'Rithvik',
    'start_date': datetime(2024, 2, 29),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'gcs_to_mongo_test',
    default_args=default_args,
    schedule=None,
    tags=["recommender"]
)

# Replace with your own values
bucket_name = 'bucket_msds697_rithvik'
json_file_path = 'crimes_data.json'
google_cloud_storage_conn_id = 'google_cloud_datastore_default'

def get_gcs_file_content(**kwargs):
    ti = kwargs['ti']
    gcs_hook = GCSHook(google_cloud_storage_conn_id)
    file_content = gcs_hook.download(bucket_name=bucket_name, object_name=json_file_path)
    file_content = file_content.decode('utf-8')
    print(file_content)
    ti.xcom_push(key='gcs_data', value=file_content)

# Python function to import data from GCS to MongoDB
def uploadtomongo(**kwargs):
    try:
        ti = kwargs['ti']
        gcs_data = ti.xcom_pull(key='gcs_data', task_ids='print_content_task')
        
        d=json.loads(gcs_data)
                
        # Connect to MongoDB
        hook = MongoHook(mongo_conn_id='mongo_default')
        client = hook.get_conn()
        db = client.MSDS697
        test_collection = db.Project1
        
        print(f"Connected to MongoDB - {client.server_info()}")
        
        # Insert data into MongoDB
        test_collection.insert_many(data_list)
        
        print("Data inserted into MongoDB successfully.")
        
    except Exception as e:
        print(f"Error uploading JSON data to MongoDB -- {e}")

get_file_gcs_task = PythonOperator(
    task_id='print_content_task',
    python_callable=get_gcs_file_content,
    provide_context=True,
    execution_timeout=timedelta(minutes=30),
    dag=dag
)

upload_to_mongodb = PythonOperator(
    task_id='upload-mongodb',
    python_callable=uploadtomongo,
    provide_context=True,
    execution_timeout=timedelta(minutes=30),
    dag=dag
)

get_file_gcs_task >> upload_to_mongodb
