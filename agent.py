import requests
import socket
import json

def send_data():
    data = {
        'host_name': socket.gethostname(),
        'ip_address': socket.gethostbyname(socket.gethostname()),
        # Add more system data here
    }
    response = requests.post('http://0.0.0.0:5065/data', json=data)
    print(response.text)

if __name__ == "__main__":
    send_data()
