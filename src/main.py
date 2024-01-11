import functions_framework
from functions import *


@functions_framework.cloud_event
def main(cloud_event):
    print("test event")
    data = cloud_event.data

    bucket = data["bucket"]
    name = data["name"]
    timeCreated = data["timeCreated"]
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

    path_url = "https://storage.googleapis.com/" + bucket + "/" + name
    # https://storage.googleapis.com/gemini-demo-images/187739b4-d12f-4bd4-b0c8-142c84636a9d.jpg

    print(path)
    # project = "cf-data-analytics"
    # loc = "us-central1"

    output = generate_text(project, loc, path)

    save_results(name, timeCreated, output, path_url)
