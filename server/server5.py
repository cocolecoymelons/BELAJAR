
import socket

import threading

import time

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

def handle_clients_request(connect_server, the_address):

  connect_server.settimeout(10)
  
  try:

    server_request = connect_server.recv(4096).decode()

    if not server_request:

      return

    first_line = server_request.split("\r\n")[0]
    method, path, version = first_line.split(" ")
    print(method,path)

    if path == "/":
  
      response = create_a_response("200 OK", "<h1>Beranda</h1><p>Selamat datang.</p>")
  
    elif path == "/halo":
  
      response = create_a_response("200 OK", "<h1>Halo!</h1>")
  
    elif path == "/tentang":
  
      response = create_a_response("200 OK","<h1>Hai, Cocolecoynut here!</h1><p>Im Cocolecoynur or Cocomelon.</p>")

    elif path == "/lambat":

      time.sleep(5)
      response = create_a_response("200 OK","<h1>Lama ya</h1>")
    
    else:
  
      response = create_a_response("404 Not Found","<h1>404 Not Found</h1><p>Halaman tidak ditemukan.</p>")
  
    connect_server.sendall(response)

  except ValueError as e:

    connect_server.sendall(create_a_response("400 Bad Request","<h1>400 Bad Request</h1><p>Format Permintaan Salah.</p>"))
    print(f"Error: {e}")
    
  except Exception as e:

    try:
      
      connect_server.sendall(create_a_response("500 Internal Server Error ","<h1>500 Internal Server Error</h1><p>Terjadi kesalahan dari dalam sistem.</p>"))
      print(f"Error: {e}")

    except Exception as socket_error:

      print(f"Gagal mengirim respon 500 karena socket telah putus: {socket_error}.")
      pass
      
  finally:

    connect_server.close()
    
while True:

  connect_server, the_address = server.accept()

  
  client_thread = threading.Thread(target=handle_clients_request, args=(connect_server, the_address),daemon=True)
  client_thread.start()