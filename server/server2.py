import socket

def create_a_response(status, body, content_type="text/html"):

  body_in_bytes = body.encode()

  header = (
    f"HTTP/1.1 {status}\r\n"
    f"Content-Type: {content_type}; charset=utf-8\r\n"
    f"Content-Length: {len(body_in_bytes)}\r\n"
    "\r\n"
  )

  return header.encode() + body_in_bytes

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("127.0.0.1", 8000))

server.listen()

while True:

  connect_server, the_address = server.accept()

  server_request = connect_server.recv(4096).decode()

  if not server_request:

    connect_server.close()
    
    continue

  first_line = server_request.split("\r\n")[0]
  method, path, version = first_line.split(" ")
  print(method,path)

  if path == "/":

    response = create_a_response("200 OK", "<h1>Beranda</h1><p>Selamat datang.</p>")

  elif path == "/halo":

    response = create_a_response("200 OK", "<h1>Halo!</h1>")

  elif path == "/tentang":

    response = create_a_response("200 OK","<h1>Hai, Cocolecoynut here!</h1><p>Im Cocolecoynur or Cocomelon.</p>")

  else:

    response = create_a_response("404 Not Found","<h1>Halaman tidak ditemukan.</h1>")

  connect_server.sendall(response)

  input("Insert untuk lepas server.")
  connect_server.close()
