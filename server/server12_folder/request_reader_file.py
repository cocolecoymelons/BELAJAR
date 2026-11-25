import socket

def read_request(connectServer):

  data = b""

  while b"\r\n\r\n" not in data:

    chunk = connectServer.recv(4096)

    if not chunk:
  
      return None, b""
  
    data += chunk

  if len(data) > 16_384:
    raise ValueError("Header is too large.")

  header_part, _, body = data.partition(b'\r\n\r\n')
  header_text = header_part.decode()

  content_length = 0
  for line in header_text.split("\r\n")[1:]:

    first_line, _, value = line.partition(":")

    if first_line.lower() == "content-length":

      content_length = int(value.strip())

  if content_length < 0 or content_length > 10_000:

    raise ValueError("Body is too large")

  while len(body) < content_length:

    chunk = connectServer.recv(4096)

    if not chunk:

      break

    body += chunk

  return header_text, body[:content_length]