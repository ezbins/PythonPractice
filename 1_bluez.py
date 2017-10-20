#!/usr/bin/env python3
# coding: utf-8

# from bluetooth import BluetoothSocket, RFCOMM
import bluetooth

serverBD = 'B8:27:EB:A5:03:6C'
port = 3
blueth = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
blueth.connect((serverBD, port))

while True:
    text = input()
    if text == 'quit':
        break
    blueth.send(text)

blueth.close()
