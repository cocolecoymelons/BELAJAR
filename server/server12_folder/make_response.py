
def make_response(page_status, body, cookie=None, location=None):

  header = [
    f"HTTP/1.1 {page_status}",
    "Content-Type: text/html; charset=utf-8",
    f"Content-Length: {len(body.encode())}",
    "Connection: close",
  ]
  
  if cookie is not None:
    header.append(f"Set-Cookie: {cookie}; lang=en; Path=/; Secure; HttpOnly; SameSite=Lax")

  if location is not None:
    header.append(f"Location: {location}")
    
  response = "\r\n".join(header) + "\r\n\r\n"

  return (response + body).encode()