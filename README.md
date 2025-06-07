# local_chat
🧩 Local Network Chat App A versatile local chat system that lets users communicate via:  

💻 Terminal-based chat for PC/Linux/Mac users  

📱 Web browser-based UI for phone users via local Wi-Fi/hotspot  

🔵 Bluetooth peer-to-peer chat for nearby devices without internet 

# Local Chat Application

A versatile local network chat application that supports multiple communication methods:
- Web interface
- Terminal client
- Bluetooth communication

## Features

- Real-time messaging with WebSockets
- Terminal-based client with commands
- Direct device-to-device communication via Bluetooth
- No internet required for local network operation

## Installation
Clone the repository:

```git clone https://github.com/gaur-avvv/local_chat.git```

```cd local_chat```

Install dependencies:

```pip install -r requirements.txt```

## Usage

### Web Server

Start the web server with:

```python server.py```

Then open a browser and navigate to `http://localhost:5000`

### Terminal Client

Run the terminal client:

`python client.py`

### Bluetooth Server

Start a Bluetooth server:

`python blue_server.py`

### Bluetooth Client

Connect to a Bluetooth server:

`python blue_client.py`



## Commands

Terminal and Bluetooth clients support these commands:
- `/exit` - Exit the chat
- `/whoami` - Display your username
- `/clear` - Clear the screen

## Requirements

- Python 3.6+
- Flask and Flask-SocketIO
- WebSocket client
- PyBluez (for Bluetooth functionality)






