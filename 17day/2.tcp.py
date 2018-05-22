from socket import *
s = socket(AF_INET,SOCK_STREAM)

s.bind(('',5656))

s.listen(5)

newSocket,clientAddr = s.accept()
while True:
    content = newSocket.recv(1024)
    print(content.decode('gb2312'))
