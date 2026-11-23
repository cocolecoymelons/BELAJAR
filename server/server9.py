
import socket, threading, traceback, html, time
import ssl


from urllib.parse import urlsplit, parse_qs

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

def create_response(page_status, body_message):

  response_message = (
    f"HTTP/1.1 {page_status}\r\n"
    "Content-Type: text/html; charset=utf-8\r\n"
    f"Content-Length: {len(body_message.encode())}\r\n"
    "\r\n"
  )

  return response_message.encode() + body_message.encode()

def read_request(connect_server):

  request_data = b""

  while b"\r\n\r\n" not in request_data:

    data_chunk = connect_server.recv(4096)

    if not data_chunk:

      return None, b""

    request_data += data_chunk

  header_part, _, body = request_data.partition(b"\r\n\r\n")

  header_text = header_part.decode()

  content_length = 0
  for line in header_text.split("\r\n")[1:]:

    first_line, _, value = line.partition(":")

    if first_line.lower() == "content-length":

      content_length = int(value.strip())

  if content_length > 10_000:

    raise ValueError("Body too large")

  while len(body) < content_length:

    data_chunk = connect_server.recv(4096)

    if not data_chunk:

      break

    body += data_chunk

  return header_text, body[:content_length]

def handle_request_func(connect_server, server_address):

  connect_server.settimeout(50)

  try:

    connect_server = context.wrap_socket(connect_server, server_side= True)

  except (ssl.SSLError, OSError) as e:

    print("TLS handshake failed.", e)

    connect_server.close()
    return
 
  try:

    header_part, httpMessageBody = read_request(connect_server)

    print("1. ",header_part, httpMessageBody)
  
    if header_part is None:
  
      print("Empty Request.")
  
      return

    first_line_of_TheRequest = header_part.split("\r\n")[0]
    method, full_path, version = first_line_of_TheRequest.split(" ")
  
    parts_of_path = urlsplit(full_path)
    path = parts_of_path.path
    
    print("2. ", parts_of_path.path)
    print("3. ", parts_of_path.query)
    
    request_query = (parse_qs(parts_of_path.query))
    print("4. ", request_query)
  
    print("5. ", method, path, version)

    if path == "/":
  
      response = create_response("200 OK","<h1>Hi, Cocolecoynut here.</h1>")

    elif path == "/login" and method == "GET":

      request_form = (
        "<h1>Login</h1>"
        "<form method='POST' action='/login'>"
        "<input name='username' placeholder='Username'>"
        "<input name='password' type='password' placeholder='Password'>"
        "<button>Login</button>"
        "</form>"
      )

      response = create_response("200 OK", request_form)

    elif path == "/login" and method == "POST":

      form_data = parse_qs(httpMessageBody.decode())

      username = form_data.get("username", [""])[0]

      response = create_response("200 OK", f"Hi {html.escape(username)}! Welcome to Cocolecoynut page.")

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
    
if __name__ == "__main__":
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  
  server.bind(("127.0.0.1",8443))
  
  server.listen()

  while True:
  
    connect_server, server_address = server.accept()
  
    print("7. ", (connect_server, server_address))
    
    client_thread = threading.Thread(target=handle_request_func,args=(connect_server,server_address),daemon=True)
    client_thread.start()
  