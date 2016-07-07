#!/usr/bin/env python3
from os import listdir, walk,chdir
from os.path import isdir, join, basename, exists,basename
import shutil,subprocess
import time
import datetime

git_bare_repo = ['branches', 'hooks']

##檢查目錄是否含有'branches','hooks'等目錄.git儲存庫才有的目錄
def checkDirectory(path):
    try:
        pathlist={}
        for root, dirs, files in walk(path):
            for signal_dir in dirs:
                fullpath = join(root, signal_dir)   
                ##當前的目錄是否有包含'branch','hook'等子目錄            
                subdirs = listdir(fullpath)
                for signal_subdir in subdirs:
                    if signal_subdir in git_bare_repo:  
                      print(fullpath)                       
                      pathlist[fullpath] = pathlist.get(fullpath,0)+1

        print(pathlist.keys())
        return pathlist                       
                       
    except OSError as error:
        print(error, end='\n')

##將檔案路徑中,取出最後一層目錄的路徑切開
def splitdirectoryPath(path):
    for singleItem in path:
        foldername = basename(singleItem)
        absPath,folder = str.split(singleItem,foldername)
        ##目錄及路徑分開後,執行備份
        excuteCommand(absPath,foldername)       


##執行外部指令
def excuteCommand(path,foldername):
    try:       
        chdir(path)       
        returnCode=subprocess.call(["tar","-zcvf",foldername+".tar.gz",foldername])
        achiveFile=foldername+'.tar.gz'
        shutil.move(achiveFile,'/home/shao')
        ##記錄執令指行的結果,
        if returnCode==0:
            chdir('/home/shao')
            logfile=open('tarfile.log','a')
            logfile.write(str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))+"\t")
            logfile.write(foldername+" was achive"+"\n")
            logfile.close()
            ##success,writing to log file
        else:
            chdir('/var/log')
            ##fault,writing to fail log file
            
    except OSError as error:
        print(error)
    


getPath = input("Enter path you wanna looking,with absu path: ")

mylist=checkDirectory(getPath)
splitdirectoryPath(mylist.keys())


