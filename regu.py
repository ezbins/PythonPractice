#!/usr/bin/python3

import re

input_data = input()
data = input_data.strip()

if re.match(r"^\d+\d$", data):
    print("match:" + data)
elif re.match(r"^\d+|[a-zA-Z]+\d+|[a-zA-Z]+$", data):
    print("match:" + data)
elif re.match(r"^\d+|[a-zA-Z!@#$%]+\d+|[a-zA-Z!@#$%]+$", data):
    print("match:" + data)
