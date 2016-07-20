#!/usr/bin/env python3

from os import mkdir,chdir
import os.path
import shutil,subprocess


wantedFolder=['RD','Eng']
try:
    if(os.path.exists('/home/scm/repositories/svn/si')):
        chdir('/home/scm/repositories/svn/si')
        for folder in wantedFolder:
            subprocess.call(["svnadmin","create",folder])
    else:
        mkdir('/home/scm/repositories/svn/si')
        chdir('/home/scm/repositories/svn/si')
        for folder in wantedFolder:
            subprocess.call(["svnadmin","create",folder])

except OSError:
    print(OSError.strerror)
