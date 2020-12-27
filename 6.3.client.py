import socket

s = socket.socket()
port = 8080
host = input("Please enter host address: ")
s.connect((host, port))
print("\nConnected to " + host)

s.close()
