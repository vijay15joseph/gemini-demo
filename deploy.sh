gcloud storage buckets create gs://gemini-cloud-function-source

gcloud storage buckets create gs://gemini-demo-images
gsutil iam ch allUsers:objectViewer gs://twillio-images