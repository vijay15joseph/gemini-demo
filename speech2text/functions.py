import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
import google.cloud
from google.cloud import speech
import vertexai.preview.generative_models as generative_models
import firebase_admin
from firebase_admin import firestore


def generate_speech2text(project_id: str, location: str, file: str) -> str:
    # Initiate Git Actions
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)
    # Initialize Speech Client
    # Instantiates a client
    # For more info on installing and using the client library, visit
    # https://cloud.google.com/speech-to-text/docs/reference/libraries
    client = speech.SpeechClient()


  
      # Load the audio file wave file into memory
    #with open(file, "rb") as audio_file:
    #    audio_content = audio_file.read()

    # transcribe speech
    audio = speech.RecognitionAudio(uri=file)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=8000,
        language_code="en-US",
        model="default",
        audio_channel_count=1,
        enable_word_confidence=True,
        enable_word_time_offsets=True,
    )

    # Detects speech in the audio file
    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)
    print(type(response.results))
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    
    transccript = ""
    for result in response.results:
        transccript += "{}".format(result.alternatives[0].transcript)
        print("Transcript: {}".format(result.alternatives[0].transcript))

    print(transccript)
   # Summarize the speech-to-text transcript using a generative AI model
    summary = summarize(transccript)
   
    
    # The response's audio_content is binary.
    return summary


def save_results(uuid, time, desc, url):
    # import firebase_admin

    # Application Default credentials are automatically created.
    # app = firebase_admin.initialize_app()

    if not firebase_admin._apps:
        firebase_admin.initialize_app()

    db = firestore.client()

    doc_ref = db.collection("gemini-demo-speech2text-summary").document(uuid)
    doc_ref.set({"timeStamp": time, "transcription": """""", "summary": desc, "speechUrl": url})


def summarize(text : str):
    vertexai.init(project="vijay-gcp-demo-project", location="us-central1")
    model = GenerativeModel("gemini-1.0-pro-001")
    print(text)
    responses = model.generate_content(
        text+"""\n
    Provide a summary of the above text in 2 sentences""",
        generation_config={
            "max_output_tokens": 2048,
            "temperature": 0.9,
            "top_p": 1
        },
        safety_settings={
            generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        },
        stream=True,
    )
    summary = ""
    
    for response in responses:
        print(response.text, end="")
        summary+="{}".response.text
    

    return summary
