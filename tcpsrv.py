import socket
import threading

bind_ip="0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)

def handle_client(client_socket):
    request = client_socket.recv(1024)

    print('[*]Received: %s' % reqiest)
    client_socket.send("ACK!")
    client_socket.close()
    
while True:
    (client,addr) = server.accept()

    client_handler=threading.Thread(target=handle_client,args=(client,))
    client_handler.start()

