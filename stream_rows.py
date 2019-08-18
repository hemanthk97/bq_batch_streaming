
from google.cloud import bigquery
from google.cloud import pubsub_v1
import json
client = bigquery.Client()
dataset_id = 'test'
table_id = 'my_data'

dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)
table = client.get_table(table_ref)

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path('linux-249818', 'casper_sub')

a = True
count = 0
while a:
    NUM_MESSAGES = 1
    response = subscriber.pull(subscription_path, max_messages=NUM_MESSAGES)
    print(len(response.received_messages),"Len on message")
    if len(response.received_messages) >= 1:
        subscriber.acknowledge(subscription_path, [response.received_messages[0].ack_id])
        print("Message received_messages ack")
        data = response.received_messages[0].message.data.decode('utf-8')
        di = json.loads(data)
        tup = (str(di['name']),str(di['price']),str(di['size']),str(di['sku']),str(di['desc']),str(di['image']),str(di['url']),str(di['rating']),str(di['review']))
        errors = client.insert_rows(table,[tup])
        assert errors == []
    else:
        print("No message")
        count = count + 1
        if count == 2:
            a = False



# for i in rows_to_insert:
#     errors = client.insert_rows(table,[i])
#     assert errors == []
