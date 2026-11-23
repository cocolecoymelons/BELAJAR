import ssl
import re
import socket, threading, time, html, traceback
from urllib.parse import parse_qs, urlsplit


context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

def make_response(page_status, body, cookie=None):

  header = [
    f"HTTP/1.1 {page_status}",
    "Content-Type: text/html; charset=utf-8",
    f"Content-Length: {len(body.encode())}",
  ]

  if cookie is not None:
    header.append(f"Set-Cookie: {cookie}")
    
  response = "\r\n".join(header) + "\r\n\r\n"

  return (response + body).encode()

def read_cookie(header_part):

  for line in header_part.split("\r\n")[1:]:
    
    first_line, _, value = line.partition(":")
    #print(f"\033[91msudah 1{first_line, value}")
    
    if first_line.lower() == "cookie":
     # print(f"ini 2{first_line}")
      chunks = value.split(";")

      for chunk in chunks:
     
        #  print(f"ini 3{chunk}")
       
        cookie_name, _, cookie_value = chunk.partition("=")

        if cookie_name.lower().strip() == "username":
        
          # print(f"4 nah ini udh dir eturn, kalau jalan hrusnya oke.{cookie_name, cookie_value}\033[0m")
          
          return cookie_value
 # print("\033[92mKalau ini jalan, somethibgs sworng\033[0m")
 
  return None
  
  
def read_request(connectServer):

  data = b""

  while b"\r\n\r\n" not in data:

    chunk = connectServer.recv(4096)

    if not chunk:
  
      return None, b""
  
    data += chunk

  header_part, _, body = data.partition(b'\r\n\r\n')
  header_text = header_part.decode()

  content_length = 0
  for line in header_text.split("\r\n")[1:]:

    first_line, _, value = line.partition(":")

    if first_line.lower() == "content-length":

      content_length = int(value.strip())

  if content_length > 10_000:

    raise ValueError("Body is too large")

  while len(body) < content_length:

    chunk = connectServer.recv(4096)

    if not chunk:

      break

    body += chunk

  return header_text, body[:content_length]
    
def handle_requests(connectServer, serverAddress):

  connectServer.settimeout(50)

  try:

    connectServer = context.wrap_socket(connectServer, server_side=True)

  except (ssl.SSLError, OSError) as e:

    print("TLS Handshake failed.", e)
    traceback.print_exc()
    connectServer.close()
    return

  try:

    headerPart, request_body = read_request(connectServer)

    if headerPart is None:

      print("Empty Request.")

      return

    first_line = headerPart.split("\r\n")[0]

    method, path, version = first_line.split(" ")

    url_parts = urlsplit(path)
    
    request_query = parse_qs(url_parts.query)
    path = url_parts.path

    if path == "/":

      response = make_response("200 OK","<h1>path '/'</h1>")

    elif path == "/login" and method == "GET":

      page = (
        "<h1>Login</h1>"
        "<form method='POST' action='/login'>"
        "<input name='username' placeholder='Username'>"
        "<input name='password' type='password' placeholder='Password'>"
        "<button>Login</button>"
        "</form>"
      )
      
      response = make_response("200 OK", page)

    elif path == "/profile" and method == "GET":

      cookie_result = read_cookie(headerPart)
      print(f"\033[92m{cookie_result}\033[0m")

      if cookie_result is None:

        connectServer.sendall(make_response("200 OK", "<h1>You are not logged in. Please log in to continue.</h1>"))

        return

      response = make_response("200 OK", f"<h1>Welcome back, {html.escape(cookie_result)}.</h1>")
    
    elif path == "/login" and method == "POST":

      form_data = parse_qs(request_body.decode())
      username = form_data.get('username', [""])[0]

      if not re.fullmatch("[a-zA-Z0-9_]{1,32}", username):

        raise ValueError("Bad request by user when insert username.")
      
      response = make_response("200 OK", f"<p>Log in success, {html.escape(username)}. <a href='/profile'>Go to profile</a></p>", f"username={username}")

    else:

      response = make_response("404 Not Found", "<h1>404 Not Found</h1><p>Your request is not found.</p>")

    connectServer.sendall(response)
  
  except ValueError as e:

    connectServer.sendall(make_response("400 Bad Request", "<h1>400 Bad Request</h1><p>Invalid request.</p>"))
    traceback.print_exc()
    print(e)

  except TimeoutError as e:
    
    connectServer.sendall(make_response("408 Request Timeout", "<h1>408 Request Timeout</h1><p>Request Timeout, please try again.</p>"))
    traceback.print_exc()
    print(e)

  except Exception as e:

    traceback.print_exc()
    print(e)
    try:

      connectServer.sendall(make_response("500 Internal Server Error", "<h1>500 Internal Server Error</h1><p>Something went wrong on our end. Please try again in a few moments.</p>"))

    except Exception as socket_error:

      print("Failed to send response, something went wrong.")
      traceback.print_exc()
    
  finally:

    connectServer.close()
    
  
if __name__ == "__main__":
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  
  server.bind(("127.0.0.1",8443))
  
  server.listen()

  while True:

    connectServer, serverAddress = server.accept()
  
    clients_threading = threading.Thread(target=(handle_requests), args=(connectServer,serverAddress),daemon=True)
    clients_threading.start()