import time
import threading
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store information about smart devices
smart_devices = {}

# Define a function to simulate a smart device
def simulate_device(device_id):
    while True:
        # Simulate device state (e.g., on/off, temperature, etc.)
        smart_devices[device_id] = {
            "status": "on" if time.time() % 2 == 0 else "off",
            "temperature": round(20 + (time.time() % 10), 2)
        }
        time.sleep(5)

# Create and start threads to simulate multiple smart devices
num_devices = 5
for i in range(num_devices):
    device_id = f"device{i}"
    threading.Thread(target=simulate_device, args=(device_id,)).start()

# Define an API endpoint to get the status of a smart device
@app.route('/api/device_status', methods=['GET'])
def get_device_status():
    device_id = request.args.get('device_id')
    if device_id in smart_devices:
        return jsonify(smart_devices[device_id])
    else:
        return "Device not found", 404

if __name__ == '__main__':
    app.run(debug=True)
