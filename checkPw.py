#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

while True:
    print('Enter passwd to check: ')
    passwd = input()
    # chek passwd length
    if passwd == '' or (len(passwd)) < 8:
        print('password is not null or password length small then 8')
        break
    pw_re = re.compile(r'''(

    )''', re.VERBOSE)
