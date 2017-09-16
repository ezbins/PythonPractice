#!/usr/bin/env python3
# coding: utf-8

from os import listdir, walk
from os.path import isdir, join, basename


def working_path(path):
    try:
        list_cotainer = listdir(path)
        for single_item in list_cotainer:
            abs_path = join(path, single_item)
            if isdir(abs_path):
                working_path(abs_path)
                if basename(abs_path) == 'General':
                    print(abs_path)
        ''' for foler_name, sub_folders, files_name in walk(path):
            print(sub_folders) '''

    except FileNotFoundError as f:
        print("FileNotFound")


path = "/home/bins"
working_path(path)
