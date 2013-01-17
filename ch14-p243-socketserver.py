import socket

s = socket.socket()
host = socket.gethostname()
ip = '192.168.1.180'
port = 1234
s.bind((ip,port))
s.listen(5)

while True:
     c, addr = s.accept()
     print ('Got connection from',addr)
     c.send('Thank you for connection'.encode())
     c.close()
