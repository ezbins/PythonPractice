#!/usr/bin/env python3
import socket

target_host = "localhost"
target_port = 8080

#建立socket物件
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立連線
client.connect((target_host,target_port))

client.send(b'hello')

data = client.recv(4096)

print('Receive',repr(data))