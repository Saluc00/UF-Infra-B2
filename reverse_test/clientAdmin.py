import socket

hote = "localhost"
port = 9999

socket = socket.socket()
socket.connect((hote, port))
print( "Connection on {}".format(port))
socket.send('ADMIN'.encode())

c= socket.recv(2048)
print(c)