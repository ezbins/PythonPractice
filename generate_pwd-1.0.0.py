#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import logging
import base64


# logging.basicConfig(level=logging.DEBUG,
#                     format=' % (asctime)s - % (levelname)s - % (message)s')


def gen_pw(lan_mac):
    raw_mac = lan_mac
    splited = raw_mac.split(':')
    str1 = '*!care@'
    conject_mac = ''
    for index in range(0, 5, 2):
        conject_mac += splited[index]

    new_str = str1 + conject_mac
    binary_string = new_str.encode('utf-8')
    encode_str = base64.b64encode(binary_string)

    return encode_str


print("Enter lan mac with ':' ->", end='')
lan_mac = '00:00:00:00:00:00'
invalid_length = True

lan_mac = input()
while invalid_length:
    if len(lan_mac) != 17:
        print("Sorry! lan mac lenght may wrong, Please key in again: ", end='')
        lan_mac = input()
        continue

    elif re.search(r'[gG]', lan_mac):
        print("Sorry! mac invalid, Please key in again: ", end='')
        lan_mac = input()
        continue

    else:
        print("{Password was inside single quote}")
        print(gen_pw(lan_mac))
        break
