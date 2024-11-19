import asyncio
import websockets
from datetime import datetime

async def simulate_call(url, duration, user_id, call_id):
    """
    Simulates a single WebSocket connection and exchanges messages for the duration specified.
    Logs messages to a separate file for each connection.
    """
    log_file = f"Call_{call_id}.log"  # Log file for this connection
    
    try:
        async with websockets.connect(url) as websocket:
            with open(log_file, "w") as file:
                file.write(f"[{datetime.now()}] Connection opened for Call ID: {call_id}\n")
            
            print(f"[{datetime.now()}] Connection opened for Call ID: {call_id}")
            
            # Message exchange
            start_time = asyncio.get_event_loop().time()
            while asyncio.get_event_loop().time() - start_time < duration:
                # Sending a message with a timestamp
                message = f"Message from {user_id} on Call ID {call_id} at {datetime.now()}"
                await websocket.send(message)
                
                log_entry = f"[{datetime.now()}] Sent: {message}\n"
                print(log_entry.strip())
                with open(log_file, "a") as file:
                    file.write(log_entry)
                
                # Receiving a response (simulated echo from server)
                response = await websocket.recv()
                log_entry = f"[{datetime.now()}] Received: {response}\n"
                print(log_entry.strip())
                with open(log_file, "a") as file:
                    file.write(log_entry)
                
                await asyncio.sleep(1)  # Simulating delay between exchanges
            
            with open(log_file, "a") as file:
                file.write(f"[{datetime.now()}] Call ID {call_id} simulation complete.\n")
            print(f"[{datetime.now()}] Call ID {call_id} simulation complete.")
    
    except Exception as e:
        error_message = f"[{datetime.now()}] Error in Call ID {call_id}: {e}\n"
        print(error_message.strip())
        with open(log_file, "a") as file:
            file.write(error_message)

async def main_simulation(base_url, user_id, num_calls, duration):
    """
    Manages multiple WebSocket connections in parallel.
    """
    tasks = []
    for call_id in range(1, num_calls + 1):
        url = f"{base_url}/{user_id}/{call_id}"
        tasks.append(simulate_call(url, duration, user_id, call_id))
    
    # Run all tasks concurrently
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Input Parameters
    BASE_URL = "ws://127.0.0.1:9001"  # Mock server URL
    USER_ID = "abc"  # Replace with the actual user ID
    NUM_CALLS = 2  # Number of simulations
    DURATION = 10  # Duration in seconds for testing

    print(f"[{datetime.now()}] Starting WebSocket simulations...")
    asyncio.run(main_simulation(BASE_URL, USER_ID, NUM_CALLS, DURATION))
    print(f"[{datetime.now()}] All simulations completed.")
