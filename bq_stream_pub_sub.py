from google.cloud import pubsub_v1
import time
# TODO project_id = "Your Google Cloud Project ID"
# TODO topic_name = "Your Pub/Sub topic name"

start_time = time.time()
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('linux-249818', 'sandiego')


url = '"https://interactive.linuxacademy.com/diagrams/TheDataDossier.html"'
desc = '"This will enable the the BigQuery Data Manipulation Language (DML) to update, insert, and delete data from the BigQuery tables Now, you can write the plain SQL query to delete the record(s)"'
for i in range(1,25):
    data = u'Hello_%d' % (i)
    # Data must be a bytestring
    data = data.encode('utf-8')
    # Add two attributes, origin and username, to the message
    future = publisher.publish(
        topic_path, data, origin='python-sample', username='gcp'
    )
    print(future.result(), i)

print('Published messages with custom attributes.')
print("--- %s seconds ---" % (time.time() - start_time))


# from google.cloud import bigquery
# client = bigquery.Client()
# filename = r'C:\Users\hemi8\Desktop\caspers_1.csv'
# dataset_id = 'demos'
# table_id = 'casper'
#
# dataset_ref = client.dataset(dataset_id)
# table_ref = dataset_ref.table(table_id)
# job_config = bigquery.LoadJobConfig()
# job_config.source_format = bigquery.SourceFormat.CSV
# job_config.skip_leading_rows = 1
# job_config.autodetect = True
# job_config.replace = False
#
#
# with open(filename, "rb") as source_file:
#     job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
#
# print("Started......")
# job.result()  # Waits for table load to complete.
#
# print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table_id))
