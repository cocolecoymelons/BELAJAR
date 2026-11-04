import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("127.0.0.1", 8000))

server.listen()

while True:

  connect,address = server.accept()

  request = connect.recv(4096).decode()

  print(request)

  if not request:
    print("Empty Connection.")
    connect.close()
    continue

  first_line = request.split("\r\n")[0]
  method, path, version = first_line.split(" ")
  print(method, path)
  
  body = "<h1>Halo server buatanku.</h1><p>Nah berubah lagi ni,sekarang jadi HTML.</p>"

  response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/html; charset=utf-8\r\n"
    f"Content-Length: {len(body.encode())}\r\n"
    "\r\n"
    + body
  )
  connect.sendall(response.encode())
  connect.close()
