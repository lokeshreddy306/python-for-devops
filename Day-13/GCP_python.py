from google.cloud import storage

export GOOGLE_APPLICATION_CREDENTIALS=""

client = storage.Client()

for bucket in client.list_buckets():
    print(bucket.name)