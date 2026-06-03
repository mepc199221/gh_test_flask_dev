from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/users", methods=["GET"])
def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True)
