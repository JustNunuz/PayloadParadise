# Reverse Shell
A **reverse shell** allows attackers to gain remote control of a target machine by having it connect back to their system, bypassing network restrictions. Its impact depends on real-world factors like network defenses and account privileges. However, the impact and effectiveness of a reverse shell depend on several factors in real-world environments:

1. **Production Environment Complexity**: In production systems, firewalls, intrusion detection systems (IDS), and endpoint protection software often monitor and block suspicious outbound traffic. A reverse shell's success may rely on the attacker disguising it as legitimate network activity, which can be challenging.

2. **Limited Privileges**: Reverse shells often inherit the permissions of the compromised account. If the compromised account has restricted privileges, the attacker may struggle to execute impactful actions without escalating privileges, which introduces additional risks of detection.

3. **Network Segmentation**: Many production environments use network segmentation to isolate critical systems. This can limit the attacker's lateral movement within the network, reducing the overall damage potential of the reverse shell.

4. **Monitoring and Logging**: Well-configured environments typically include logging and monitoring solutions. Suspicious behavior from a reverse shell, such as unusual commands or outbound connections, can trigger alerts and allow defenders to respond quickly.

5. **Persistence Challenges**: Establishing persistence to maintain access is another hurdle. Sophisticated environments implement patch management, endpoint detection, and system integrity checks that can disrupt or remove the reverse shell.

In summary, while a reverse shell can provide attackers with significant control over a compromised system, real-world production environments often present numerous barriers that reduce its immediate impact. Effective security practices like least privilege, segmentation, and proactive monitoring can greatly diminish the damage a reverse shell can cause.

### **File and Directory Management**

These commands allow you to manipulate files, delete, duplicate, etc.

| Command                   | Description                                        |
| ------------------------- | -------------------------------------------------- |
| `dir`                     | Lists files and directories in the current folder. |
| `cd [path]`               | Changes the current directory.                     |
| `md [foldername]`         | Creates a new directory.                           |
| `rd [foldername]`         | Removes a directory (must be empty).               |
| `del [filename]`          | Deletes a file.                                    |
| `copy [source] [dest]`    | Copies files to a new location.                    |
| `move [source] [dest]`    | Moves files to a new location.                     |
| `ren [oldname] [newname]` | Renames a file or folder.                          |
| `tree`                    | Displays a graphical tree of directories.          |

---

### **System and User Management**

These commands help manage users, privileges, system shutdowns, and tasks.

| Command                                         | Description                                         |
| ----------------------------------------------- | --------------------------------------------------- |
| `whoami`                                        | Displays the current username.                      |
| `hostname`                                      | Shows the computer's hostname.                      |
| `tasklist`                                      | Lists running processes.                            |
| `taskkill /pid [ID]`                            | Ends a process by its process ID.                   |
| `shutdown /s /t [time]`                         | Schedules a shutdown after a set time (in seconds). |
| `shutdown /r`                                   | Restarts the system.                                |
| `net user`                                      | Displays user accounts.                             |
| `net user [username] /add`                      | Adds a new user.                                    |
| `net localgroup administrators [username] /add` | Grants admin rights.                                |

---

### **Network Commands**

These commands provide network-related information and diagnostics.

| Command             | Description                               |
| ------------------- | ----------------------------------------- |
| `ipconfig`          | Displays network adapter settings.        |
| `ipconfig /all`     | Shows detailed network configuration.     |
| `ping [host]`       | Tests connectivity to a host.             |
| `tracert [host]`    | Traces the route to a host.               |
| `netstat -an`       | Displays active network connections.      |
| `nslookup [domain]` | Resolves a domain to its IP address.      |
| `arp -a`            | Shows the ARP cache.                      |
| `net view`          | Displays shared resources on the network. |

---

### **System Information and Troubleshooting**

| Command                   | Description                                  |
| ------------------------- | -------------------------------------------- |
| `systeminfo`              | Displays detailed system information.        |
| `sfc /scannow`            | Scans and repairs corrupted system files.    |
| `chkdsk [drive:]`         | Checks and repairs disk errors.              |
| `diskpart`                | Opens disk management command-line tool.     |
| `driverquery`             | Lists installed drivers.                     |
| `powercfg /batteryreport` | Generates a battery health report (laptops). |
| `eventvwr`                | Opens Event Viewer.                          |

---

### **PowerShell-Specific**

| Command                        | Description                           |
| ------------------------------ | ------------------------------------- |
| `Get-Process`                  | Lists running processes.              |
| `Get-Service`                  | Lists services and their statuses.    |
| `Set-ExecutionPolicy [policy]` | Changes script execution permissions. |
| `Get-ChildItem` (alias: `ls`)  | Lists directory contents.             |
| `Measure-Object`               | Calculates properties of objects.     |
| `Export-Csv`                   | Exports data to a CSV file.           |

---

### **Windows Subsystem for Linux (WSL)**

| Command                      | Description                                |
| ---------------------------- | ------------------------------------------ |
| `wsl`                        | Opens the default WSL instance.            |
| `wsl --list`                 | Lists installed WSL distributions.         |
| `wsl --install`              | Installs WSL and the default Linux distro. |
| `wsl --set-default [distro]` | Sets the default WSL distribution.         |

---

### **Shortcut and Helpful Commands**

| Command           | Description                                  |
| ----------------- | -------------------------------------------- |
| `cls`             | Clears the screen.                           |
| `exit`            | Exits the terminal.                          |
| `echo [text]`     | Prints text to the terminal.                 |
| `start [program]` | Opens a program or file.                     |
| `help`            | Displays available commands in the terminal. |


