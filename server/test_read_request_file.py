from server8 import read_request

class FakeConnection:

  def __init__(self, chunks):

    self.chunks = list(chunks)

  def recv(self, n):

    return self.chunks.pop(0) if self.chunks else b""

header, body = read_request(FakeConnection([b"GET /xy HTTP/1.1\r\nContent-Length: 5\r\n\r\nhello"]))

assert header == "GET /xy HTTP/1.1\r\nContent-Length: 5" and body == b"hello", (header,body)

print("1. OK: All required data is complete.")

header, body = read_request(FakeConnection([b"GET /xy HTTP/1.1\r\nContent", b"-Length: 5\r\n\r\nhel", b"lo"]))

assert header == "GET /xy HTTP/1.1\r\nContent-Length: 5" and body == b"hello", (header, body)

print("2. OK: All required data is complete(Some data was truncated when getting a request.)")

header, body = read_request(FakeConnection([b"POST /xy HTTP/1.1\r\nContent-Length: 5\r\n\r\n"]))

assert header == "POST /xy HTTP/1.1\r\nContent-Length: 5" and body == b"", (header, body)

print("3. OK: HTTP Message didn't contain body.")

header, body = read_request(FakeConnection([]))

assert header is None and body == b""

print("4.OK: HTTP Message is missing.")

try:
  header, body = read_request(FakeConnection([b"POST /xy HTTP/1.1\r\nContent-Length: 1234321234321\r\n\r\nhello"]))

  assert header == "POST /xy HTTP/1.1\r\nContent-Length: 1234321234321" and body == b"hello", (header,body)

except ValueError as e:

  print("5. OK: Message body length exceeded.")

header, body = read_request(FakeConnection([b"GET /xy HTTP/1.1\r\nContent-Length:5\r\n\r\nhel"]))

print("6.OK: Message body length is less than the Content Length.")