from socket import *
a = socket(AF_INET, SOCK_DGRAM)
a.sendto('那思源'.encode('gb2312'),('192.168.43.116',7777))

a.close()
