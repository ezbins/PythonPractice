#!/usr/bin/env python3

import os

#取得所有正規檔案
names = [name for name in os.listdir('/home/shao') if os.path.isfile(os.path.join('/home/shao',name))]

#取得所有目錄
dirnames = [name for name in os.listdir('/home/shao') if os.path.isdir(os.path.join('/home/shao',name))]

for filename in names:
    print(filename)

print("above are directories")

for dirname in dirnames:
    print(dirname)