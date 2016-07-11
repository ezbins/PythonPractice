#!/usr/bin/python3.4
import sys

for path in sys.path:
     print(path)


for m in sys.modules:
     print(m, end='\n')