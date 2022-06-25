import pickle
import urllib.request

from flask import Flask
from flask import request
from flask import jsonify

PICKLE_URL = "https://raw.github.com/Heimrych/predict_american_tweets/main/model.pickle"

# PORT = 5013
app = Flask(__name__)
app.model = pickle.load(urllib.request.urlopen(PICKLE_URL))
# app.model = pickle.load(open("model.pickle", "rb"))

@app.route("/api/american", methods=["POST"])
def return_prediction():
    request_data = request.get_json(force=True)
    text = request_data['text']
    prediction = app.model.predict([text])
    american = "American" if prediction[0] else "Not American"
    return jsonify(
        version_number="0.2",
        prediction=american
    )
