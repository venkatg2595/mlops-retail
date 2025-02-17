from flask import Flask, request, jsonify
import mlflow.pyfunc

app = Flask(__name__)

model = mlflow.pyfunc.load_model("models:/RetailModel/1")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    predictions = model.predict(data["features"])
    return jsonify(predictions.tolist())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
