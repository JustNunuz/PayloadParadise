# C2 Server Configurations (Raspberry Pi / Linux)

This folder contains the server-side components needed to catch data exfiltrated by the payloads in this repository. 

Rather than relying on public services (like Pastebin), which can block IPs or remove content, setting up your own Command & Control (C2) server on a Raspberry Pi or Linux VPS ensures you have full control over the exfiltrated data.

---

## 1. The Simple TCP Listener (Netcat)

The most lightweight method. The server opens a raw TCP port and waits for the payload to send data directly over a socket.

### Setup on the Pi:
No installation required. `nc` (Netcat) is pre-installed on almost all Linux distributions.
To listen on port `9001` and save all incoming data to a text file, run:

```bash
nc -lvnp 9001 > exfiltrated_data.txt
```

* **Pros:** Zero setup, universally available, incredibly fast.
* **Cons:** Firewalls often block outgoing connections to non-standard ports (like 9001) or raw TCP traffic that doesn't look like web traffic.
* **Payload Code Requirement:** The payload only needs the target IP and Port to establish a `socket` connection.

---

## 2. The HTTP POST Receiver (Python Flask)

This method simulates a legitimate web server. The payload sends data via an HTTP POST request (just like submitting a form on a website).

### Setup on the Pi:
1. Install Flask:
   ```bash
   pip install flask
   ```
2. Create a file named `http_receiver.py` (provided in this folder).
3. Run the server:
   ```bash
   python3 http_receiver.py
   ```

* **Pros:** Highly resilient. Port 80 (HTTP) and 443 (HTTPS) are almost never blocked by outgoing firewalls. You can easily format and organize incoming data.
* **Cons:** Requires a small amount of setup (installing Flask).
* **Payload Code Requirement:** The payload uses Python's standard `urllib` to send an HTTP POST request to `http://<PI_IP>:<PORT>/upload`.

---

## How to use with Payloads

Once your server (either Netcat or Flask) is running, you simply modify the `PI_IP` or `PI_URL` variable inside the corresponding payload script (like the Wi-Fi Harvester) to point to your Raspberry Pi's local network IP address (e.g., `192.168.1.55`) or its public IP if exposed to the internet.
