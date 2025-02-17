from google.cloud import bigquery

def load_data_to_bigquery():
    client = bigquery.Client()
    dataset_id = 'your_project.your_dataset'
    table_id = f'{dataset_id}.retail_data'
    uri = 'gs://your_bucket/retail_data.csv'
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        autodetect=True
    )
    load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
    load_job.result()
    print("Data successfully loaded to BigQuery.")