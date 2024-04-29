from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

data_store = []  # This will store the data temporarily

@app.route('/')
def home():
    return "Cybersecurity Monitoring App"

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    data_store.append(data)  # Store data
    return jsonify({"status": "Data received"}), 200

@app.route('/data', methods=['GET'])
def send_data():
    return jsonify(data_store)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5065)
