#encoding: utf-8
from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21568
ADDR = (HOST, PORT)

class MyRequestHandle(SRH):
    def handle(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))
tcpServ = TCP(ADDR, MyRequestHandle)
print 'waiting for connection...'
tcpServ.serve_forever()
