import socket
import threading
import traceback
import html
import time
from urllib.parse import urlsplit, parse_qs

def create_response(page_status, body_message):

  response_message = (
    f"HTTP/1.1 {page_status}\r\n"
    "Content-Type: text/html; charset=utf-8\r\n"
    f"Content-Length: {len(body_message.encode())}\r\n"
    "\r\n"
  )

  return response_message.encode() + body_message.encode()    
  
def handle_request_func(connect_server, server_address):

  connect_server.settimeout(50)

  try:

    server_request = connect_server.recv(4096).decode()

    print(server_request)
  
    if not server_request:
  
      print("Empty Request.")
  
      connect_server.close()
  
      return

    first_line_of_therequest = server_request.split("\r\n")[0]
    method, full_path, version = first_line_of_therequest.split(" ")
  
    parts_of_path = urlsplit(full_path)
    path = parts_of_path.path
    
    print(parts_of_path.path)
    print(parts_of_path.query)
    
    request_query = (parse_qs(parts_of_path.query))
    print(request_query)
  
    print(method, path, version)

    if path == "/":
  
      response = create_response("200 OK","<h1>Hi, Cocolecoynut here.</h1>")

    elif path == "/halo":

      name = request_query.get("name", ["Anonymous"])[0]
      response = create_response("200 OK", f"<h1>Halo {html.escape(name)}!</h1>")
  
    elif path == "/cocolecoynut":
  
      response = create_response("200 OK","<h1>About Cocolecoynut</h1><p lang='en'>Cocomelons aka Cocolecoynut is a developer from Indonesia striving to be the best human alive.</p>")
  
    else:
  
      response = create_response("404 Not Found","<h1>404 Page Not Found</h1><p>Page is not found.</p>")

    connect_server.sendall(response)

  except ValueError as e:

    connect_server.sendall(create_response("400 Bad Request","<h1>400 Bad Request</h1><p>Bad request</p>"))
    traceback.print_exc()

    print(e)

  except Exception as e:

    try:
      
      connect_server.sendall(create_response("500 Internal Server Error","<h1>500 Internal Server Error</h1><p>There's something wrong with our server. Please try again later.</p>"))
      traceback.print_exc()

    except Exception as socket_error:

      print("Failed to send response due to disconnected socket.")
      pass

  finally:

    connect_server.close()
    

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("127.0.0.1",8000))

server.listen()

while True:

  connect_server, server_address = server.accept()

  print((connect_server, server_address))
  
  client_thread = threading.Thread(target=handle_request_func,args=(connect_server,server_address),daemon=True)
  client_thread.start()
  
  

  