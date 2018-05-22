from socket import *

# 创建socket
s = socket(AF_INET, SOCK_STREAM)
s.connect(('192.168.1.117',6688))


# 链接服务器
while True:

# 提示用户输入数据
    senddata = input("请输入要发送的数据：")

    s.send(senddata.encode('gb2312'))

# 接收对方发送过来的数据，最大接收1024个字节
recvData = s.recv(1024)
print(recvData.decode('gb2312'))

# 关闭套接字
s.close()
