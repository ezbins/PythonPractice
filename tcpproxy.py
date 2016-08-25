#!/usr/bin/env python3

import sys
import socket
import threading

def server_loop(local_host,local_port,remote_host,remote_port,receive_first):
    
    srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        srv.bind((local_host,local_port))
    except:
        print("[!!] Failed to listen %s:%d" % (local_host,local_port))
        print("[!!] Check for other listening sockets or correct permissions.")
        sys.exit(0)

    print("[*] Listening on %s:%d" %(local_host,local_port))

    srv.listen(5)

    while True:
        client_socket,addr = srv.accept()

        #print out local connection information
        print("[==>] Received imcoming connection from %s:%d" % (addr[0],addr[1]))

        #start a thread to talk to remote host
        proxy_thread = threading.Thread(target=proxy_handler,args=(client_socket,remote_host,remote_port,receive_first))
        proxy_thread.start()
