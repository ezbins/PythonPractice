#!/usr/bin/env python3
# coding: utf-8

from os import listdir, walk, chdir, remove
from os.path import isdir, join, basename
import shutil
import subprocess


# 備份專案,tar檔型式

def backup_tar_file(path):
    try:
        chdir(path)
        total_folders = listdir(path)
        for folder_name in total_folders:
            subprocess.call(
                ["tar", "zcvf", folder_name + ".tar.gz", folder_name])
            shutil.copy(folder_name + ".tar.gz", '/tmp')
            remove(folder_name + ".tar.gz")
    except OSError:
        print("backup failed")


def working_path(path):
    try:
        list_cotainer = listdir(path)
        for single_item in list_cotainer:
            abs_path = join(path, single_item)
            if isdir(abs_path):
                if basename(abs_path) in ['si', 'sd']:
                    backup_tar_file(abs_path)
                    ''' chdir(abs_path)
                    open('foo.txt', 'wt')
                    print(listdir(abs_path)) '''
                else:
                    working_path(abs_path)

    except FileNotFoundError as f:
        print("FileNotFound")


path = "/home/shao/pyexec"
working_path(path)
