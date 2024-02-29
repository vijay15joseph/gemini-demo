# gcloud storage buckets create gs://gemini-cloud-function-source

gcloud storage buckets create gs://gemini-demo-images --location=us-central1; gcloud storage buckets add-iam-policy-binding gs://gemini-demo-images --member=allUsers --role=roles/storage.objectViewer


gcloud storage buckets create gs://cf-gemini-demo-app-host --location=us-central1
gcloud storage buckets add-iam-policy-binding gs://cf-gemini-demo-app-host --member=allUsers --role=roles/storage.objectViewer
gcloud storage cp web/ gs://cf-gemini-demo-app-host -r

gcloud firestore indexes composite create --collection-group=gemini-demo-images --field-config=field-path=timeStamp,order=descending --field-config=field-path=imageDescription,order=ascending

