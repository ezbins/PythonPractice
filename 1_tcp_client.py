#!/usr/bin/env python3
# coding: utf-8

import socket
import json

target_host = "127.0.0.1"
target_port = 81

# 建立socket物件
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 讓client 連線
client.connect((target_host, target_port))
# 傳送一些資料
data = {'hello': 'I transfer json data','hello2':'add to values'}

json_obj = json.dumps(data)
client.sendall(json_obj.encode('utf-8'))
response = client.recv(4096)
print(response)
