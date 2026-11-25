import socket

from concurrent.futures import ThreadPoolExecutor
from response_handler_file import handle_requests
  
if __name__ == "__main__":
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  
  server.bind(("127.0.0.1",8443))
  
  server.listen()

with ThreadPoolExecutor(max_workers=10) as exe:
  
  while True:

    connectServer, serverAddress = server.accept()
  
    exe.submit(handle_requests, connectServer,serverAddress)