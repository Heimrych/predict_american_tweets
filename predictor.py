import pickle

from flask import Flask
from flask import request
from flask import jsonify

# PORT = 5013
app = Flask(__name__)
app.model = pickle.load(open("model.pickle", "rb"))

@app.route("/api/american", methods=["POST"])
def return_prediction():
    request_data = request.get_json(force=True)
    text = request_data['text']
    prediction = app.model.predict([text])
    american = "American" if prediction[0] else "Not American"
    return jsonify(
        prediction=american
    )