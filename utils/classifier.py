
import pickle

model = pickle.load(
    open(
        "model/document_classifier.pkl",
        "rb"
    )
)

def classify_document(text):

    prediction = model.predict([text])[0]

    probabilities = model.predict_proba([text])[0]

    confidence = max(probabilities) * 100

    categories = model.classes_

    return (
        prediction,
        probabilities,
        confidence,
        categories
    )

