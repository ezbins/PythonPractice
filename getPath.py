#!/usr/bin/env python3
from os import listdir
from os.path import isdir, join, basename


def checkDirectory(path):
    for single_item in listdir(path):
        fullname = join(path, single_item)
        if isdir(fullname):
            print(basename(fullname), end='\n')


checkDirectory("/tmp")
