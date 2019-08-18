import time

from google.cloud import pubsub_v1

# TODO project_id = "Your Google Cloud Project ID"
# TODO subscription_name = "Your Pub/Sub subscription name"

subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_name}`
subscription_path = subscriber.subscription_path(
    'linux-249818', 'sub1')

def callback(message):
    print('Received message: {}'.format(message.data))
    message.ack()

subscriber.subscribe(subscription_path, callback=callback)

# The subscriber is non-blocking. We must keep the main thread from
# exiting to allow it to process messages asynchronously in the background.
print('Listening for messages on {}'.format(subscription_path))
while True:
    time.sleep(60)
