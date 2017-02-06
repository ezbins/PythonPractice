#!/usr/bin/env python3
# coding=utf-8

import re

while True:
    print('Enter passwd to check: ')
    passwd = input()
    # chek passwd length
    if passwd == '' or (len(passwd)) < 8:
        print('password is not null or password length small then 8')
        break
    if re.search("[\d{8}]", passwd):
        print('weak password')
        break
    # if re.search("[\w{8}]", passwd):
    #     print('weak password')
    #     break
    if not re.search("[!@#$%^&*]", passwd):
        print('weak passwd')
        break
    else:
        print('complex password')
        break
    # pw_re = re.compile(r'''(
    #     [a-zA-z\d{1:}]+
    # )''', re.VERBOSE)
    # if pw_re.search(passwd):
    #     print("Complex password")
    # else:
    #     print("weak password")
