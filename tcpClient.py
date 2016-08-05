#!/usr/bin/env python3

import  socket


target_host='tw.yahoo.com'
target_port=80

#建立socket物件
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立連線
client.connect((target_host,target_port))

#傳送一些資料
client.send(b'GET https://tw.yahoo.com\r\nHTTP/2.0')

data = client.recv(4096)

print('Receive',repr(data))
