#!/usr/bin/env python3
from os import listdir, walk
from os.path import isdir, join, basename, exists,basename
import shlex, subprocess

git_bare_repo = ['branches', 'hooks']


def checkFiles(path):
    for root, dirs, files in walk(path):
        for filename in files:
            fullname = join(root, filename)
            print(fullname, end='\n')


##檢查目錄是否含有'branches','hooks'等目錄.git儲存庫才有的目錄
def checkDirectory(path):
    try:
        for root, dirs, files in walk(path):
            for signal_dir in dirs:
                subpath = join(root, signal_dir)               
                subdirs = listdir(subpath)
                for item in subdirs:
                    if item in git_bare_repo:                       
                      pathlist = dict({subpath:1})
                      return pathlist                       
                       
    except OSError as error:
        print(error, end='\n')

##將檔案路徑中,取出最後一層目錄的路徑切開
def splitdirectoryPath(path):
    for singleItem in path:
        folder = basename(singleItem)
        absPath = str.split(singleItem,'folder')
        ##目錄及路徑分開後,執行備份
        excuteCommand(absPath,folder)
        print (name)


##執行外部指令
def excuteCommand(path,folder):
    try:
        os.chdir(path)
        command_line="tar zcvf "+folder+".tar.gz "+folder+"\\/"
        args=shlex.split(command_line)
        subprocess.Popen(args)
        
    except OSError as error:
        print(error)
    
getPath = input("Enter path you wanna looking,with absu path: ")
mylist=checkDirectory(getPath)

splitdirectoryPath(mylist.keys())
