import functions_framework
from functions import *
import os


@functions_framework.cloud_event
def main(cloud_event):
    # trigger data
    data = cloud_event.data

    bucket = data["bucket"]  # bucket
    name = data["name"]  # file name
    timeCreated = data["timeCreated"]  # time when file was created

    project = os.getenv('PROJECT')
    loc = os.getenv('LOCATION')

    # project = "cf-data-analytics"  # required to initialize vertex client
    # loc = "us-central1"
    path = "gs://" + bucket + "/" + name  # uri

    path_url = "https://storage.googleapis.com/" + bucket + "/" + name  # public url

    # function that calls gemini api for speech2text transcription
    output = generate_speech2text(project, loc, path)

    # save gemini output as document to firestore
    save_results(name, timeCreated, output, path_url)
