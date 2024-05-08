#agent.py
import requests
import socket
import json
import psutil

def get_system_metrics():
#collect metrics
    return {
        'cpu_usage': psutil.cpu_percent(interval=1),
        'disk': {
            'total': psutil.disk_usage('/').total,
            'used': psutil.disk_usage('/').used,
            'free': psutil.disk_usage('/').free
        },
        'memory': {
            'total': psutil.virtual_memory().total,
            'used': psutil.virtual_memory().used,
            'available': psutil.virtual_memory().available
        }
    }

def send_data():
    #collect system data and send to server
    data = {
        'host_name': socket.gethostname(),
        'ip_address': socket.gethostbyname(socket.gethostname())
    }
    # Include additional system metrics
    data.update(get_system_metrics())

    response = requests.post('http://192.168.0.19:5065/data', json=data)
    print(response.text)

if __name__ == "__main__":
    send_data()
