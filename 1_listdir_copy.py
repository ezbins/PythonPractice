#!/usr/bin/env python3
# coding: utf-8

from os import listdir, walk, chdir, remove, mkdir
from os.path import isdir, join, basename, exists, isfile
from shutil import copy
import time
import datetime


# 移動tar檔到備份目錄
def copy_tar_file(path, backup_path):
    try:
        chdir(path)
        total_folders = listdir(path)
        for item_name in total_folders:
            if isfile(join(path, item_name)):
                copy(item_name, backup_path)
                remove(item_name)

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
                    if not exists("/repobackup/" + basename(abs_path)):
                        backup_path = mkdir(
                            "/repobackup/" + basename(abs_path))
                    else:
                        backup_path = "/repobackup/" + basename(abs_path)

                    copy_tar_file(abs_path, backup_path)
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
