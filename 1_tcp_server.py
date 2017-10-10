#!/usr/bin/env python3
# coding: utf-8

import socket
import threading
import json

bind_ip = "0.0.0.0"
bind_port = 81

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)


def handle_client(client_socket):
    # 顯示送來的資料
    request = client_socket.recv(1024)
    # raw_receive_data = str(request)
    receive_data = json.loads(request.decode('utf-8'))
    for key in receive_data.keys():
        print("[*] Received: %s" % receive_data[key])
    # 回傳一個封包
    client_socket.sendall("ACK!".encode("utf-8"))
    client_socket.close()


while True:
    client, addr = server.accept()
    print("[*] Acccept connection from %s:%d" % (addr[0], addr[1]))
    # 啟動client thread
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

