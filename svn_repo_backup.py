#!/usr/bin/env python3


from os import listdir, walk, chdir, remove
from os.path import isdir, join, basename, exists, basename, dirname
import shutil
import subprocess
import time
import datetime


def checkDirectory(path):
    try:
        subdirs = listdir(path)
        for singleDir in subdirs:
            absPath = dirname(singleDir)
            excuteCommand(path, singleDir)

    except OSError as e:
        chdir('/var/log')
        logfile = open('badNews.log', 'a')
        logfile.write(str(datetime.datetime.fromtimestamp(
            time.time()).strftime('%Y-%m-%d %H:%M:%S')) + "\t")
        logfile.write(e.strerror + "\n")


# 將檔案路徑中,取出最後一層目錄的路徑切開
def splitdirectoryPath(path):
    for itemOfList in path:
        # 取得目錄名稱
        foldername = basename(itemOfList)
        # 取得目錄的父目錄路徑
        absPath = dirname(itemOfList)
        # 目錄及路徑分開後,執行備份
        excuteCommand(absPath, foldername)


# 執行外部指令
def excuteCommand(path, foldername):
    try:
        chdir(path)
        returnCode = subprocess.call(
            ["tar", "-zcvf", foldername + ".tar.gz", foldername])
        achiveFile = foldername + '.tar.gz'
        shutil.copy(achiveFile, '/repobackup')
        remove(achiveFile)
        # 記錄執令指行的結果,
        if returnCode == 0:
            chdir('/var/log')
            logfile = open('tarfile.log', 'a')
            logfile.write(str(datetime.datetime.fromtimestamp(
                time.time()).strftime('%Y-%m-%d %H:%M:%S')) + "\t")
            logfile.write(foldername + " was archived" + "\n")
            logfile.close()

    except OSError as e:
        chdir('/var/log')
        logfile = open('badNews.log', 'a')
        logfile.write(str(datetime.datetime.fromtimestamp(
            time.time()).strftime('%Y-%m-%d %H:%M:%S')) + "\t")
        logfile.write(e.strerror + "\n")


checkDirectory('/home/scm/repositories/svn/')
