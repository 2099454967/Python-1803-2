from socket import *

from threading import Thread
s = None
ip = ''
port = 0

def send():
    while True:
        content = input('请输入发送的内容:')
        s.sendto(content.encode('gb2312'),(ip,port))

def recv():
    while True:
        msg = s.recvfrom(8888)
        print('s%---s%'%(msg[0].decode('gb2312'),msg[1][0]))

def main():
    global s
    global ip
    global port
    ip = input('亲输入ip:')
    port = int(input('请输入对方端口:'))
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(('',6667))
    t = Thread(target = send)

    t.start()

    t.join()
    t1 = Thread(target = recv)
    t1.start()
    t1.join()

if __name__ == '__main__':
    main()

