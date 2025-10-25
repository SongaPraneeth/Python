import socket
import sys
from datetime import datetime

try:
  remote_server  = input("Enter the target: ")
  remote_server_IP = socket.gethostbyname(remote_server)

  t1 = datetime.now()
  
  print("-"*60)
  print(f"Scanning IP address:{remote_server_IP}")
  print("-"*60)

  for port in range(1,1024):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.settimeout(0.5) 
      result = sock.connect_ex((remote_server_IP, port))
      if result == 0:
        print(f"[+] port {port} is open")
    
except KeyboardInterrupt:
  print("scan as been interrupted")
  sys.exit()

except socket.gaierror:
  print("Host name could not be resolved.")
  sys.exit()

except socket.error:
  print("Failed to connect to server")
  sys.exit()

finally: 
  t2 = datetime.now()

  time_taken = t2-t1
  print(f"Scan completed in: {time_taken}")