import socket
import sys
import time
import threading
import os

from datetime import datetime


def port_scan():
    IP = input("[*] ~ Enter IP Address: ")
    # Banner
    print("-" * 52)
    print("[*] Scanning IP Address: " + IP)
    print("[*] Scanning started at: " + str(datetime.now()))
    print("-" * 52)
    ports = []
    # Script for detecting all of the open ports on the server(IP)
    def scan(port):
        # Create sockets   
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        try:
            # Return open ports
            connection.connect((IP, port))
            connection.close()
            print(f"[+] Port [ {port} ] is open.")
            ports.append(port)
        except Exception:
            pass
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit()

    try:
        scanned = 1
        # Scan every port on the server 
        for port in range(1, 65500): # Valid port range for all systems
            thread = threading.Thread(target=scan, kwargs={'port':scanned})
            scanned += 1
            thread.start()
            # time.sleep(0.0001)
    except KeyboardInterrupt:
        print("\n[*] Exiting...")
        sys.exit()
        
    print("-" * 50)
    print(f"[*] {scanned} ports were scanned.")
    print("[*] Open ports: " + str(ports))
