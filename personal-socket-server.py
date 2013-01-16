import socket

s = socket.socket()
_HOST  = socket.gethostname()
_PORT  = 1234
try:
    s.bind((_HOST,_PORT))
    s.listen(5)
    (conn, addr) = s.accept()
    while True:
        
        rec_msg = conn.recv(1024).decode()
        print ('recived: ' + rec_msg)
        if rec_msg.strip().lower() == 'bye':
            conn.send ('bye from server!'.encode())
            break
        replymsg = 'Hello' + str(conn)
        conn.send(replymsg.encode())
        print ('send: ' + replymsg)
finally:
    conn.close()
