import requests
import socket
import psutil
import time
import speedtest

#Differences in client version:
# Removed the WebSocket logic to simplify data collection and sending.
# Metrics are sent directly to the PostgreSQL server via the Flask endpoint.
# Adjusted the sleep interval to 10 seconds for less frequent measurements.

# Flask server URL to send data for PostgreSQL storage
FLASK_URL = "http://192.168.0.19:5065/data"

def get_ip_address():
    """Get the IP address of the host system."""
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception:
        return "Unknown"

def measure_internet_speed():
    """Measure the internet speed using Speedtest."""
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping  # Get the ping in ms

        return {
            'download_speed_mbps': download_speed,
            'upload_speed_mbps': upload_speed,
            'ping_ms': ping
        }
    except Exception as e:
        print(f"Error measuring internet speed: {e}")
        return {
            'download_speed_mbps': 0,
            'upload_speed_mbps': 0,
            'ping_ms': 0
        }

def collect_and_send_metrics():
    """Collect system metrics periodically and send them to the Flask server for PostgreSQL storage."""
    while True:
        # Collect CPU, memory, network, and internet speed metrics
        network_io = psutil.net_io_counters()
        internet_speed = measure_internet_speed()  # Get internet speed data

        metrics = {
            'host_name': socket.gethostname(),
            'ip_address': get_ip_address(),
            'cpu_usage': psutil.cpu_percent(interval=1),
            'memory': {
                'total': psutil.virtual_memory().total,
                'used': psutil.virtual_memory().used,
            },
            'network': {
                'bytes_sent': network_io.bytes_sent,
                'bytes_recv': network_io.bytes_recv,
                'packets_sent': network_io.packets_sent,
                'packets_recv': network_io.packets_recv,
                'err_in': network_io.errin,
                'err_out': network_io.errout,
                'drop_in': network_io.dropin,
                'drop_out': network_io.dropout,
            },
            'internet_speed': internet_speed
        }

        # Send data to the Flask server for PostgreSQL storage
        try:
            response = requests.post(FLASK_URL, json=metrics)
            response.raise_for_status()  # Raise an error if the request failed
            print(f"Data successfully sent to {FLASK_URL}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending data to {FLASK_URL}: {e}")

        # Interval between each data collection
        time.sleep(10)

if __name__ == "__main__":
    collect_and_send_metrics()
