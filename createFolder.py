#!/usr/bin/env python3

from os import mkdir,chdir
import os.path
import shutil,subprocess


wantedFolder=['RD','Eng']
projects = ['TWCAXXX130501','TWCA000160401','TWLC001160501','TWCH001160501','TWHO000131101',
            'TWHO002131101','TWHO002140901','TWCL000151001','TWCH000160701','TWCA001160601']
try:
    if(os.path.exists('/home/scm/repositories/svn/si')):    
        chdir('/home/scm/repositories/svn/si')
        for parentFolder in projects:
            for subFolder in wantedFolder:
                fullPath=str(parentFolder)+'/'+str(subFolder)
                subprocess.call(["mkdir","-p",fullPath])
                subprocess.call(["svnadmin","create",fullPath])
    else:
        mkdir('/home/scm/repositories/svn/si')
        chdir('/home/scm/repositories/svn/si')
        for parentFolder in projects:
            for subFolder in wantedFolder:
                fullPath=str(parentFolder)+'/'+str(subFolder)
                subprocess.call(["mkdir","-p",fullPath])
                subprocess.call(["svnadmin","create",fullPath])

except OSError as e:
    print(e.strerror)
