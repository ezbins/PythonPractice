#!/usr/bin/env python3
# coding: utf-8

from os import listdir, walk, chdir, remove, mkdir
from os.path import isdir, join, basename
import shutil
import subprocess
import time
import datetime


# SVN儲存庫壓縮
def backup_svn_repo(path, backup_path):
    try:
        chdir(path)
        total_folders = listdir(path)
        for item_name in total_folders:
            subprocess.call(["tar", "zcvf", item_name + ".tar.gz", item_name])

    except OSError as e:
        chdir("/var/log")
        logfile = open('tar_files.log', 'a')
        logfile.write(str(datetime.datetime.fromtimestamp(
            time.time()).strftime('%Y-%m-%d %H:%M:%S')) + "\t")
        logfile.write(e.strerror + "\n")


def working_path(path):
    try:
        list_cotainer = listdir(path)
        backup_path = ""
        for single_item in list_cotainer:
            abs_path = join(path, single_item)
            if isdir(abs_path):
                if basename(abs_path) in ['si', 'sd']:
                    backup_svn_repo(abs_path, backup_path)
                else:
                    working_path(abs_path)

    except FileNotFoundError as f:
        chdir('/var/log')
        logfile = open('badNews.log', 'a')
        logfile.write(str(datetime.datetime.fromtimestamp(
            time.time()).strftime('%Y-%m-%d %H:%M:%S')) + "\t")
        logfile.write(e.strerror + "\n")


path = "/home/scm/repositories/svn"
working_path(path)
