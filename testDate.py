#!/usr/bin/env python3

import time
import datetime

print(time.time())
print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))