#encoding: utf-8

from socket import *
from time import ctime

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print 'waiting for connection...'
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    if data:
        print data
    udpSerSock.sendto('[%s] %s' % (ctime(), data))
    print '...received from and returned to: ', addr
udpSerSock.close()

