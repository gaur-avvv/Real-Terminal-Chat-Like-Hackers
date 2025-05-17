import websocket
import threading
import json
from datetime import datetime

username = input("Enter your username: ")

def on_message(ws, message):
    print("\n" + message + "\n> ", end="")

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("Disconnected.")

def on_open(ws):
    def send_loop():
        while True:
            msg = input("> ")
            if msg == "/exit":
                ws.close()
                break
            elif msg == "/whoami":
                print(f"You are {username}")
                continue
            elif msg == "/clear":
                print("\033c", end="")
                continue
            timestamp = datetime.now().strftime('%H:%M')
            ws.send(json.dumps({"username": username, "message": msg}))
    threading.Thread(target=send_loop).start()

if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://localhost:5000/socket.io/?EIO=4&transport=websocket",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
