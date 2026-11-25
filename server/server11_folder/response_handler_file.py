import socket, time, html, re, traceback, ssl
from urllib.parse import parse_qs, urlsplit

from cookie_reader_file import read_cookie
from request_reader_file import read_request
from make_response import make_response

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="../cert.pem", keyfile="../key.pem")


def handle_requests(connectServer, serverAddress):

  connectServer.settimeout(15)

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
      
      response = make_response("303 See Other", "", f"username={username}", "/profile")

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