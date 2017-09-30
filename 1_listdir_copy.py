#!/usr/bin/env python3
# coding: utf-8

from os import listdir, walk, chdir, remove, mkdir
from os.path import isdir, join, basename, exists, isfile
import subprocess
import time
import datetime


wanted_to_move_file_path = "/home/scm/repositories/svn"
move_file_dest = "/repobackup/"


# 移動tar檔到備份目錄
def copy_tar_file(path, backup_path):
    try:
        chdir(path)
        total_folders = listdir(path)
        for item_name in total_folders:
            if isfile(join(path, item_name)):
                subprocess.call(["mv", item_name, backup_path])

    except OSError as e:
        chdir("/var/log")
        logfile = open('copy_tar_files.log', 'a')
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
                    if not exists(move_file_dest + basename(abs_path)):
                        backup_path = mkdir(
                            move_file_dest + basename(abs_path))
                    else:
                        backup_path = move_file_dest + basename(abs_path)

                    copy_tar_file(abs_path, backup_path)
                else:
                    working_path(abs_path)

    except FileNotFoundError as f:
        chdir('/var/log')
        logfile = open('badNews.log', 'a')
        logfile.write(str(datetime.datetime.fromtimestamp(
            time.time()).strftime('%Y-%m-%d %H:%M:%S')) + "\t")
        logfile.write(e.strerror + "\n")


working_path(wanted_to_move_file_path)
