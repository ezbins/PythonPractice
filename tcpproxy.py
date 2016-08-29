#!/usr/bin/env python3

import sys
import socket
import threading

def receive_from(connection):
    buffer =""
    #we set a 2 second time out depending on you target
    #this my need to be adjusted
    connection.settimeout(2)

    try:
        #keep reading data into the buffer until there're no more data
        #or we time out
        while True:
            data = connection.recv(4096)

            if not data:
                break
            buffer+=data

    except:
        pass
    
    return buffer
    
def request_handler(buffer):
    return buffer

def response_handler(buffer):
    return buffer

def proxy_hanlder(client_socket,remote_host,remote_port,receive_first):
    remote_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    remote_socket.connect((remote_host,remote_port))

    #receive data from remote end if necessary
    if receive_first:
        
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

        #send it to our response handler
        remote_buffer = response_handler(remote_buffer)

        #if any data send to local client send it
        if len(remote_buffer):
            print("[<==] Sending %d bytes to localhost" % len(remote_buffer))
            client_socket.send(remote_buffer)

    while True:
        
        #read from locals
        local_buffer = receive_from(client_socket)

        if len(local_buffer):
            print("[==>]Receive %d bytes from localhost." % len(local_buffer))
            hexdump(local_buffer)

            #send it to request handle
            local_buffer = request_handler(local_buffer)

            #send it to remote target
            remote_host.send(local_buffer)
            print("[==>] Send to remote.")

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

def main():
    
    if len(sys.argv[1:]) != 5:
        print("Usage:./tcpproxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]")
        print("Example ./tcpproxy.py 127.0.0.1 9000 10.21.213.1 9000 True")
        sys.exit(0)
    
    #setting localhost information
    local_host = sys.argv[1]
    local_port = int(sys.argv[2])

    #setting remotehost information
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])

    #告訴tcpproxy 先連上遠端主機,接收資料再傳回來
    receive_first = sys.argv[5]

    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False

    #now spin up our listening socket
    server_loop(local_host,local_port,remote_host,remote_port,receive_first)

main()
