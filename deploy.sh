# gcloud storage buckets create gs://gemini-cloud-function-source

gcloud storage buckets create gs://gemini-demo-images --location=us-central1
gsutil iam ch allUsers:objectViewer gs://gemini-demo-images