from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "WebSocket Server Running"

@socketio.on('update_metrics')
def handle_metrics(data):
    """Broadcast the latest data to all clients."""
    # Debugging: Print received data
    print(f"Received metrics: {data}")
    socketio.emit('live_update', data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5066)
