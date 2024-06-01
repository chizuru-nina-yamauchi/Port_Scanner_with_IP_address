import socket  # Importing the socket module for network communication
from datetime import datetime  # Importing datetime module to work with dates and times

# Define the target IP address to scan. User input is used here.
target = input("Enter the IP address to scan: ")

# Print a banner to provide information about the target and when the scan started
print("-" * 60)
print(f"Scanning target {target}")
print("Time started:", str(datetime.now()))  # Printing the current date and time
print("-" * 60)

# Function to scan a single port
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a socket object for TCP connections
    socket.setdefaulttimeout(1)  # Setting a default timeout of 1 second for socket operations
    result = s.connect_ex((target, port))  # Attempting to connect to the target IP address and port
    if result == 0:
        print(f"Port {port}: Open")  # If the connection was successful, print that the port is open
    s.close()  # Close the socket after the operation is complete

# Using a loop to specify ports to scan (from 1 to 1024)
try: #(try-except block to handle exceptions)
    for port in range(1, 1025): # Looping through ports from 1 to 1024
        scan_port(port)  # Calling the scan_port function for each port in the specified range
except KeyboardInterrupt:
    print("\nExiting program.")  # Handling the KeyboardInterrupt exception (Ctrl+C)
except socket.gaierror:
    print("\nHostname could not be resolved.")  # Handling errors related to hostname resolution
except socket.error:
    print("\nServer not responding.")  # Handling general socket errors

print("-" * 60)
print("Scan completed.")
print("-" * 60)
