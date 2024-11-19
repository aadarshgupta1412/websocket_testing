from websocket_server import WebsocketServer
from datetime import datetime

def new_client(client, server):
    print(f"[{datetime.now()}] New client connected: {client}")

def handle_message(client, server, message):
    print(f"[{datetime.now()}] Received from client {client['id']}: {message}")
    server.send_message(client, f"Echo: {message}")

def client_left(client, server):
    print(f"[{datetime.now()}] Client disconnected: {client}")

server = WebsocketServer(host='127.0.0.1', port=9001)
server.set_fn_new_client(new_client)
server.set_fn_message_received(handle_message)
server.set_fn_client_left(client_left)

print(f"[{datetime.now()}] Mock WebSocket server running on ws://127.0.0.1:9001")
server.run_forever()
