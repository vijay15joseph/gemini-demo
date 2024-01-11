import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
import firebase_admin
from firebase_admin import firestore


def generate_text(project_id: str, location: str, file: str) -> str:
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)
    # Load the model
    multimodal_model = GenerativeModel("gemini-pro-vision")
    # Query the model
    response = multimodal_model.generate_content(
        [
            # Add an example image
            Part.from_uri(
                file, mime_type="image/jpeg"
            ),
            # Add an example query
            "what is shown in this image?",
        ]
    )
    print(response)
    return response.text


def save_results(time, desc, url):
    import firebase_admin

    # Application Default credentials are automatically created.
    app = firebase_admin.initialize_app()
    db = firestore.client()

    doc_ref = db.collection("gemini-demo-images").document("test_doc")
    doc_ref.set({"first": "Chas", "last": "Lovelace", "born": 1815})
