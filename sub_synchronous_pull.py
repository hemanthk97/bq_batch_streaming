from google.cloud import pubsub_v1

# TODO project_id = "Your Google Cloud Project ID"
# TODO subscription_name = "Your Pub/Sub subscription name"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(
    'linux-249818', 'sub1')

NUM_MESSAGES = 5

# The subscriber pulls a specific number of messages.
response = subscriber.pull(subscription_path, max_messages=NUM_MESSAGES)

for message in response.received_messages:
    print(message.message.data)
    subscriber.acknowledge(subscription_path, [message.ack_id])
    print(message.message.data,"ACK")
