import firebase_admin
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter


def results():

    if not firebase_admin._apps:
        firebase_admin.initialize_app()

    db = firestore.client()

    cities_ref = db.collection("gemini-demo-images")
    query = cities_ref.order_by(
        "timeStamp", direction=firestore.Query.DESCENDING).limit(6)
    results = query.stream()

    outputArray = []
    outputDict = {}

    for doc in results:
        outputArray.append(doc.to_dict())

    outputDict["data"] = outputArray

    return outputDict


def text_results():

    if not firebase_admin._apps:
        firebase_admin.initialize_app()

    db = firestore.client()

    results = (db.collection("gemini-demo-text-result")
               .where(filter=FieldFilter("timeStamp", "!=", "null"))
               .order_by("timeStamp", direction=firestore.Query.DESCENDING)
               .limit(10)
               .get())

    outputArray = []
    outputDict = {}

    for doc in results:
        outputArray.append(doc.to_dict())

    outputDict["data"] = outputArray

    return outputDict
