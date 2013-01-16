import socket

s = socket.socket()
_HOST = socket.gethostname()
_PORT = 1234
try:
    s.connect((_HOST,_PORT))
    #s.send('Hello'.encode())
    while True:
        
        send_msg = input ('Input ur message!')
        print ('send: ' + send_msg)
        s.sendall(send_msg.encode())
        rec_msg = s.recv(1024).decode()
        print ('recived: ' + rec_msg)
        if rec_msg.strip().lower() == 'bye from server!':
            break

finally:
    s.close()
