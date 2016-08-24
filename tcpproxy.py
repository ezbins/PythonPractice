#!/usr/bin/env python3

import sys
import socket
import threading

def server_loop(local_host,local_port,remote_hote,remote_port,receive_first):
    
    srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:

    except:

    print("[*] Listening on %s:%d" %(local_host,local_port))

    srv.listen(5)
