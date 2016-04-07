import os

os.chdir("/home/shao")
try:
    data = open(".vimrc")
    for text in data:
        text.strip()
        print(text, end='')
except OSError:
    print("Sorry!! No file was found..")
