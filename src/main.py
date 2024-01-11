import functions_framework
from functions import *


@functions_framework.cloud_event
def main(cloud_event):
    print("test event")
    data = cloud_event.data

    # event_id = cloud_event["id"]
    # event_type = cloud_event["type"]

    bucket = data["bucket"]
    name = data["name"]
    # metageneration = data["metageneration"]
    # timeCreated = data["timeCreated"]
    # updated = data["updated"]

    # print(f"Event ID: {event_id}")
    # print(f"Event type: {event_type}")
    # print(f"Bucket: {bucket}")
    print(f"File: {name}")
    # print(f"Metageneration: {metageneration}")
    # print(f"Created: {timeCreated}")
    # print(f"Updated: {updated}")

    project = "cf-data-analytics"
    loc = "us-central1"
    path = "gs://" + bucket + "/" + name
    print(path)
    # project = "cf-data-analytics"
    # loc = "us-central1"

    generate_text(project, loc, path)

    save_results("")
