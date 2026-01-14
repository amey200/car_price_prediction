from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("car_price_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    year = int(data["year"])
    present_price = float(data["present_price"])
    kms = int(data["kms"])
    fuel = int(data["fuel"])
    seller = int(data["seller"])
    transmission = int(data["transmission"])
    owner = int(data["owner"])

    input_data = np.array([[year, present_price, kms, fuel, seller, transmission, owner]])
    prediction = model.predict(input_data)[0]

    return jsonify({"price": round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)
