
from urllib.parse import urlsplit, parse_qs

parts = urlsplit("/halo?nama=Cocomelon&umur=25")

print(parts)
print(parts.path)
print(parts.query)
print(parse_qs(parts.query))