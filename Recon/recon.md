### Reconnaissance Script Overview

This script is designed to perform a comprehensive system reconnaissance on a target machine by collecting various pieces of system information and exfiltrating the data to a remote server. Reconnaissance is a key phase in penetration testing and ethical hacking, as it allows the attacker or tester to gather valuable insights into the target system's environment.

### Script Functionality

1. **System Metadata Collection**:  
   The `collect_system_metadata` function collects essential information about the system, including:
   - **Operating system**: Name, version, and release
   - **System architecture**: Whether it's 32-bit or 64-bit
   - **Hostname**: The name of the machine
   - **IP address**: The machine's local IP address
   - **Current user**: The logged-in user
   - **Boot time**: The time the system was last booted

2. **Running Processes**:  
   The `get_running_processes` function retrieves a list of all active processes running on the system, including:
   - **PID** (Process ID)
   - **Process name**
   - **Username**: The user under which the process is running

3. **Network Information**:  
   The `get_network_info` function collects network interface and connection details, including:
   - **Network interfaces** and their respective addresses
   - **Active connections** with details such as local and remote addresses, connection status, and the associated process IDs (PIDs)

4. **Disk Usage**:  
   The `get_disk_usage` function retrieves disk usage statistics for each partition on the system, including:
   - **Total space**
   - **Used space**
   - **Free space**
   - **Usage percentage** for each disk partition

5. **Environment Variables**:  
   The `get_environment_variables` function collects all environment variables present on the system, which may contain useful information about the system configuration and user-specific settings.

6. **Data Exfiltration**:  
   After collecting the data, the script converts the collected information into a JSON format and sends it to a remote server using the `exfiltrate_data_via_tcp` function. The script connects to the server at the specified IP (`192.168.100.2`) and port (`9001`) using a TCP connection and sends the collected data.

### Reconnaissance

Reconnaissance is the process of gathering information about a target system or network to understand its configuration and identify potential vulnerabilities. There are two main types of reconnaissance:

- **Passive Reconnaissance**:  
   This involves gathering information without directly interacting with the target system, such as:
   - Monitoring network traffic
   - Gathering publicly available information (e.g., domain information, website metadata)
   - Using tools like `whois` and `nslookup`

- **Active Reconnaissance**:  
   This involves directly interacting with the target system to collect information, such as:
   - Scanning for open ports and services using tools like `nmap`
   - Enumerating network shares and other accessible resources
   - Using tools like Metasploit for exploitation testing

### Usage in a Network

This reconnaissance script is particularly useful for active reconnaissance within a network. Once the data is collected and exfiltrated, the attacker or penetration tester can:
- Analyze the system's configuration to identify potential vulnerabilities
- Identify running services and their corresponding entry points
- Analyze open network connections and potential lateral movement paths
- Assess disk usage to identify sensitive or valuable data locations
- Review environment variables for possible misconfigurations or sensitive information (e.g., passwords, API keys)