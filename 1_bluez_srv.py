#!/usr/bin/env python3
# coding: utf-8

from bluetooth import BluetoothSocket

host_BD = 'B8:27:EB:A5:03:6C'
port = 3
backlog = 2
size = 1024
blueth = BluetoothSocket(bluetooth.RFCOMM)
blueth.bind((host_BD, port))
blueth.listen(backlog)


try:
    client, client_info = blueth.accept()
    while True:
        data = client.recv(1024)
        if data:
            print(data)

except:
    print("Closing socket")
    client.close()
    blueth.close()