#!/usr/bin/env python3
import os.path
import os
import shlex, subprocess

path="/home/shao"

absPath,folder=str.split(path,'CPAN')
try:
    os.chdir(path)
    path=os.getcwd()
    print("current path is "+path)
    # command_line="touch abc.txt"
    # args=shlex.split(command_line)
    foldername='javascript'
    #p=subprocess.Popen(args,stdout=True)
    returnCode=subprocess.call(["tar","-zcvf",foldername+".tar.gz",foldername])
    print(returnCode)
    #filename="abc.txt"
    if os.path.isfile('abc.txt'):
        print("file exist")
    else:
        print("file does not exist")
    #print(p)
   
except OSError as error:
    print("Can not change to "+error )

# print(absPath)
# print(folder)
