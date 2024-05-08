#stripped down version w/o visuals runs on server.
import json

from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from visualizations import plot_disk_usage, plot_memory_usage, plot_cpu_usage

# # Database connection
# connection = psycopg2.connect(
#     database="fanclub_data",
#     user="postgres",
#     password="XXXXXXXX",
#     host="localhost",
#     port="5432"
# )

cursor = connection.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS raw_data (
        id SERIAL PRIMARY KEY,
        hostname VARCHAR(255),
        ip_address VARCHAR(45),
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        raw_data JSONB
    )
""")
connection.commit()

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/')
def home():
    return "Cybersecurity Monitoring App"

@app.route('/data', methods=['POST'])
def receive_data():
    # Receive and store raw data in the database
    data = request.get_json()
    json_data = json.dumps(data)  # Convert dict to JSON string

    cursor.execute(
        """
        INSERT INTO raw_data (hostname, ip_address, raw_data)
        VALUES (%s, %s, %s)
        """,
        (data.get('host_name'), data.get('ip_address'), json_data)
    )
    connection.commit()
    return jsonify({"status": "Data received"}), 200

@app.route('/data', methods=['GET'])
def send_data():
    # Return all collected data from the database
    cursor.execute("SELECT * FROM raw_data")
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/visualizations/disk', methods=['GET'])
def visualize_disk():
    # Save disk data to file
    output_path = '/Users/connerjordan/Desktop/disk_usage.png'
    last_entry = data_store[-1] if data_store else None

    if last_entry:
        plot_disk_usage(last_entry['disk'], output_path)
        return jsonify({"status": "Disk usage plot generated", "file": output_path}), 200
    else:
        return jsonify({"error": "No data available"}), 404

@app.route('/visualizations/memory', methods=['GET'])
def visualize_memory():
    # Save memory data to file
    output_path = '/Users/connerjordan/Desktop/memory_usage.png'
    last_entry = data_store[-1] if data_store else None

    if last_entry:
        plot_memory_usage(last_entry['memory'], output_path)
        return jsonify({"status": "Memory usage plot generated", "file": output_path}), 200
    else:
        return jsonify({"error": "No data available"}), 404

@app.route('/visualizations/cpu', methods=['GET'])
def visualize_cpu():
    # Save CPU data to file
    output_path = '/Users/connerjordan/Desktop/cpu_usage.png'
    last_entry = data_store[-1] if data_store else None

    if last_entry:
        plot_cpu_usage(last_entry['cpu_usage'], output_path)
        return jsonify({"status": "CPU usage plot generated", "file": output_path}), 200
    else:
        return jsonify({"error": "No data available"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5065)
