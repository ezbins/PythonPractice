#!/usr/bin/env python3
# coding: utf-8

import traceback


def find_biggest(list):
    if not list:
        return 0
    else:
        max = find_biggest(list[1:])
        return max if max > list[0] else list[0]


list = [34, 108, 56, 78, 98]
print(find_biggest(list))
