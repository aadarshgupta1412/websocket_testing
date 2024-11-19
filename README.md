# **WebSocket Testing System**

This project provides a **WebSocket testing system** that simulates multiple client-server interactions for testing purposes. The system includes a mock WebSocket server that echoes client messages and a client simulation script that creates multiple WebSocket connections, sends messages, and logs all activity.

---

## **Contents**
1. `mock_websocket_server.py`  
   - A mock WebSocket server that listens on `ws://127.0.0.1:9001`.
   - Echoes back any messages received from clients.
     
2. `simulate_websockets.py`  
   - Simulates multiple WebSocket connections to the server.
   - Sends text-based messages with timestamps to the server.
   - Logs all sent and received messages to separate log files for each connection.

---

## **Requirements**
- **Python** 3.7 or later.
- Install the required libraries:
  ```bash
  pip install websocket
  pip install websocket-server
  ```

## **Usage**

### Step 1: Start the Mock WebSocket Server
Run the server in one terminal:

```bash
python mock_websocket_server.py
```

- The server will listen on `ws://127.0.0.1:9001`.
- Logs events (e.g., connections, disconnections, and messages) in the terminal.

### Step 2: Run the Client Simulation
In another terminal, run the client simulation:

```bash
python simulate_websockets.py
```

- The client script will:
  - Open multiple WebSocket connections (default: 2 connections).
  - Exchange messages with the server for a specified duration (default: 10 seconds).
  - Create log files (`Call_<call_id>.log`) for each connection in the script directory.

## **Configuration**
You can customize the behavior of the client simulation in `simulate_websockets.py`: 

**Number of Connections:**
Change the `NUM_CALLS` variable to set how many connections to simulate:

```python
NUM_CALLS = 5  # Number of simulated WebSocket calls
```

**Duration of Each Call:**
Adjust the `DURATION` variable to set how long each call lasts (in seconds):

```python
DURATION = 60  # Call duration in seconds
```

**Base WebSocket URL:**
Update `BASE_URL` if your server is running on a different host or port:

```python
BASE_URL = "ws://<your_server_host>:<your_server_port>"
```

## **Output**

- **Server Logs:**
  View server events (e.g., connections, messages) in the terminal running `mock_websocket_server.py`.

- **Client Logs:**
  Each connection generates a separate log file (`Call_<call_id>.log`) containing the exchange of messages with timestamps. Example:

```plaintext
[2024-11-19 12:00:01] Connection opened for Call ID: 1
[2024-11-19 12:00:01] Sent: Message from abc on Call ID 1 at 2024-11-19 12:00:01
[2024-11-19 12:00:01] Received: Echo: Message from abc on Call ID 1 at 2024-11-19 12:00:01
[2024-11-19 12:00:11] Call ID 1 simulation complete.
```
