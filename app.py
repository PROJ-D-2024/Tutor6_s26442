from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

def predict(x):
    return 2 * x + 3 

@app.route("/predict", methods=["POST"])
def predict_endpoint():
    data = request.get_json()
    x = np.array(data["input"])
    result = predict(x)
    return jsonify({"prediction": result.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
