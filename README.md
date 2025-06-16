# Local Chat Application

A versatile local network chat application that supports multiple communication methods, allowing users to communicate via a web interface, a terminal client, or direct Bluetooth connection.

## Features

-   **Multiple Communication Modes:**
    -   Network chat (Wi-Fi/Ethernet): Supports a web-based UI accessible from any device on the local network (including phones) and a terminal-based client for PC/Mac/Linux users.
    -   Bluetooth chat: Enables direct peer-to-peer communication between two nearby devices without needing a network infrastructure.
-   **Real-time Messaging:** Leverages WebSockets for instant message delivery in network mode.
-   **Terminal Client Commands:** Offers commands like `/exit`, `/whoami`, and `/clear` for an enhanced terminal chat experience.
-   **No Internet Required:** Fully functional on a local network or via Bluetooth without an internet connection.

## Requirements

-   Python 3.6+
-   Bluetooth adapter (for Bluetooth chat feature).
-   All other Python package dependencies are listed in `requirements.txt`.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/gaur-avvv/local_chat.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd local_chat
    ```
3.  **Install dependencies:**
    This will install all necessary Python packages, including Flask, Flask-SocketIO, PyBluez, etc.
    ```bash
    pip install -r requirements.txt
    ```
    *Note for Bluetooth on Linux:* You might need to install additional system packages like `python3-bluez` or `libbluetooth-dev` (e.g., `sudo apt-get install libbluetooth-dev`).

## Usage

This application offers two main modes of communication:

### 1. Network Chat (Wi-Fi/Ethernet)

This mode uses your local network (Wi-Fi or Ethernet) to connect clients to a central server.

**A. Start the Server:**
Run the server script. This will host both the web UI and the WebSocket server for terminal clients.
```bash
python server.py
```

- The server will start on 0.0.0.0:5000. It will also print instructions on how to find your machine's local IP address. You'll need to share this IP address with other users on your network who want to connect.

- Finding Your Server's IP Address: To allow other users on your local network to connect to the server, they need its IP address. The server script will display common commands to find it when it starts.

Here's a summary:

Windows: Open Command Prompt and type ipconfig. Look for the 'IPv4 Address'.

Linux: Open a terminal and type ip addr or hostname -I.

macOS: Open Terminal and type ifconfig. Look for the 'inet' address.

B. Connect with a Client:

Users have two options to connect:

- Web Client: Open a web browser and navigate to http://<server_ip>:5000 (replace <server_ip> with the actual IP address of the machine running server.py). This is suitable for all devices, including mobile phones.

- Terminal Client: Run the terminal client script:

```python client.py```
The client will prompt you to enter the server's IP address. Enter the IP address of the machine where ```server.py``` is running.

2. Bluetooth Chat
This mode allows for direct peer-to-peer communication between two Bluetooth-enabled devices.


## Requirements & Setup:

```bash
PyBluez: Ensure PyBluez is installed '(it's in requirements.txt).'

Bluetooth Enabled: Make sure Bluetooth is enabled on both devices.

Device Pairing & Discoverability: For best results, devices should be paired at the operating system level before attempting to connect via the application. Ensure your device is discoverable by other Bluetooth devices.
```

## How to Run:

Start the Bluetooth Server: One user starts the Bluetooth server script:

python blue_server.py
The server will advertise the "BluetoothChatService" and wait for a connection, printing the RFCOMM channel it's using.

Start the Bluetooth Client: The other user runs the Bluetooth client script:

python blue_client.py
The client will search for nearby Bluetooth devices, list them, and then attempt to find and connect to the "BluetoothChatService" on the selected device.

## Important Notes for Bluetooth Chat:

Two Users Only: The current Bluetooth scripts are designed for a one-to-one chat session.

Reliability: Bluetooth connectivity can vary based on OS, drivers, hardware, and distance. If you encounter issues:

Confirm devices are paired at the OS level.

Try restarting Bluetooth on both devices.

Ensure the server script is running and successfully advertised the service.

Check the console for any Bluetooth-related error messages on both client and server.

## Commands
The Terminal Client (for Network Chat) and the Bluetooth Client support the following commands:
```bash
/exit - Quit the chat application.

/whoami - Display your current username.

/clear - Clear the terminal screen.
