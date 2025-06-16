from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(data):
    username = data.get('username', 'Anonymous')
    message = data.get('message', '')
    timestamp = datetime.now().strftime('%H:%M')
    full_message = f"[{timestamp}] {username}: {message}"
    print(full_message)
    send(full_message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
    print("\nServer is running on 0.0.0.0:5000.")
    print("Clients on your local network can connect to you using your machine's local IP address.")
    print("To find your IP address:")
    print("  - On Windows: Open Command Prompt and type 'ipconfig'")
    print("  - On Linux: Open a terminal and type 'ip addr' or 'hostname -I'")
    print("  - On macOS: Open Terminal and type 'ifconfig'")
    print("Share this IP address with other users.\n")
