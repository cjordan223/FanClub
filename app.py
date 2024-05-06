from flask import Flask, request, jsonify
from flask_cors import CORS
from visualizations import plot_disk_usage, plot_memory_usage, plot_cpu_usage

app = Flask(__name__)
CORS(app)  # Enable CORS

# Temporary storage for collected data
data_store = []

@app.route('/')
def home():
    return "Cybersecurity Monitoring App"

@app.route('/data', methods=['POST'])
def receive_data():
    """Receives and stores data sent by agents."""
    data = request.get_json()
    data_store.append(data)
    return jsonify({"status": "Data received"}), 200

@app.route('/data', methods=['GET'])
def send_data():
    """Returns all collected data."""
    return jsonify(data_store)

@app.route('/visualizations/disk', methods=['GET'])
def visualize_disk():
    """Visualizes disk usage of the last received data."""
    if data_store:
        last_entry = data_store[-1]  # Use the latest data
        plot_disk_usage(last_entry['disk'])
        return jsonify({"status": "Disk usage plot generated"}), 200
    else:
        return jsonify({"error": "No data available"}), 404

@app.route('/visualizations/memory', methods=['GET'])
def visualize_memory():
    """Visualizes memory usage of the last received data."""
    if data_store:
        last_entry = data_store[-1]
        plot_memory_usage(last_entry['memory'])
        return jsonify({"status": "Memory usage plot generated"}), 200
    else:
        return jsonify({"error": "No data available"}), 404

@app.route('/visualizations/cpu', methods=['GET'])
def visualize_cpu():
    """Visualizes CPU usage of the last received data."""
    if data_store:
        last_entry = data_store[-1]
        plot_cpu_usage(last_entry['cpu_usage'])
        return jsonify({"status": "CPU usage plot generated"}), 200
    else:
        return jsonify({"error": "No data available"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5065)
