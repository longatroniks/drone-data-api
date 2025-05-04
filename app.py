from flask import Flask, jsonify, redirect, url_for
import csv
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

def load_assets():
    assets = []
    with open("assets.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            assets.append({
                "id": row["ID"],
                "name": row["Name"],
                "type": row["Type"],
                "latitude": float(row["Latitude(Y)"]),
                "longitude": float(row["Longitude(X)"])
            })
    return assets

@app.route("/api/assets", methods=["GET"])
def get_assets():
    return jsonify(load_assets())

@app.route("/", methods=["GET"])
def home():
    return redirect(url_for('get_assets'))

if __name__ == "__main__":
    app.run(debug=True)
