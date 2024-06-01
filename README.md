# Port Scanner with IP address(Simple ethical hacking experiment with Python)

## Overview
This Python script serves as a simple ethical hacking experiment, allowing users to scan ports on a specified IP address to identify open ports. It utilizes the socket module to create TCP sockets and establish connections to each port within a specified range.

## Requirements
- Python 3.x

## Usage
1. Clone the repository or download the Python script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the Python script.
4. Run the script by executing the command:

```
python port_scanner.py
```

5. Follow the prompts to enter the target IP address.
6. The script will scan ports 1 to 1024 on the specified IP address and display the results.

## Understanding the code
- The socket module is used for creating network sockets, allowing the script to establish TCP connections to each port.
- TCP (Transmission Control Protocol) connections are established to determine whether each port on the target IP address is open or closed.
- The script utilizes error handling to gracefully handle exceptions such as KeyboardInterrupt and socket errors.

## Disclaimer
This script is intended for educational purposes only. Do not use it for any malicious activities. Always seek permission before scanning ports on a network or IP address.