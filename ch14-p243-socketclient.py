import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
ip = '192.168.1.180'
s.connect((ip,port))
print (s.recv(1024).decode())
