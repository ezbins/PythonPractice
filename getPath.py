#!/usr/bin/env python3
from os import listdir, walk
from os.path import isdir, join, basename, exists

git_bare_repo = ['branches', 'hooks']


def checkFiles(path):
    for root, dirs, files in walk(path):
        for filename in files:
            fullname = join(root, filename)
            print(fullname, end='\n')


def checkDirectory(path):
    try:
        for root, dirs, files in walk(path):
            for signal_dir in dirs:
                subpath = join(root, signal_dir)
                print(type(subpath))
                subdirs = listdir(subpath)
                for item in subdirs:
                    if item in git_bare_repo:
                         print(subpath, end='\n')
                         pathlist = dict( subpath= "1")
                         return pathlist

                        # print(item, end='\n')
                        # print(subpath, end='\n')
                # print(subdirs,end='\n')
                # if signal_dir in git_bare_repo:
                #      next
                # else :
                #      fullDir=join(root,signal_dir)
                #      print(fullDir,end='\n')
    except OSError as error:
        print(error, end='\n')

getPath = input("Enter path you wanna looking,with absu path: ")
mylist=checkDirectory(getPath)

for key, value in mylist.items():
     print(key,value, end='\n')
