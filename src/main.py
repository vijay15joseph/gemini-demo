import functions_framework
from functions import *


@functions_framework.cloud_event
def main(cloud_event):
    print("test")
    # data = cloud_event.data

    # event_id = cloud_event["id"]
    # event_type = cloud_event["type"]

    # bucket = data["bucket"]
    # name = data["name"]
    # metageneration = data["metageneration"]
    # timeCreated = data["timeCreated"]
    # updated = data["updated"]

    # print(f"Event ID: {event_id}")
    # print(f"Event type: {event_type}")
    # print(f"Bucket: {bucket}")
    # print(f"File: {name}")
    # print(f"Metageneration: {metageneration}")
    # print(f"Created: {timeCreated}")
    # print(f"Updated: {updated}")

    # gcs_bucket = bucket
    # gcs_file = name
    # table_id = "cf-data-analytics.spark_example.gcf_stream"

    # x = read_from_gcs(gcs_bucket,gcs_file)

    # print(type(x))
    # print(x)

    # write_to_bq(x,table_id)

    # delete_blob(gcs_bucket, gcs_file)
