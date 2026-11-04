import socket
#import random
#import dataclasses

print(dir(socket))

print([n for n in dir(socket.socket) if not n.startswith("_")])
print(dir(socket.socket.getsockopt))
#print(dir(random))
#print(dir(dataclasses))

print(socket.gethostbyname("google.com"))
