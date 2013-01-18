from socketserver import TCPServer, StreamRequestHandler,ThreadingMixIn

class Server(TCPServer,ThreadingMixIn):pass

class Handler(StreamRequestHandler):

     def handle(self):
          addr = self.request.getpeername()
          print ('Get connection from: '+str(addr))
          self.data  = self.request.recv(1024).strip()
          self.wfile.write('Thank u'.encode()+self.data)
          print ('Get msg: '+self.data.decode() )
#server = TCPServer(('',1234),Handler)

server = Server(('',1234),Handler)
server.serve_forever()
